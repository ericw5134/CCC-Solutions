#include <bits/stdc++.h>
using namespace std;
typedef long long ll;

const int maxn = 1e6 + 233;
ll c[maxn], dp[maxn], mxdp[maxn];

void update(int i, ll val)
{
    for(int x = maxn - i - 1; x < maxn; x += x & -x) c[x] = max(c[x], val); 
}

ll suffixAsk(int i)
{
    ll ret = 0;
    for(int x = maxn - i - 1; x; x -= x & -x) ret = max(ret, c[x]);
    return ret;
}

int day[maxn], a[maxn];
int ma[maxn]; // max suffix a[] value of prevoius day
int n, k;

int main()
{
    scanf("%d%d", &n, &k);
    for(int i = 1; i <= n; i++) scanf("%d", &a[i]);
    for(int i = n%k, j = 1; i <= n; i += k) day[j++] = i;
    for(int i = 1, today = 1, back = 0, _maxa = 0; i <= n; i++)
    {
        int lim = day[today - 1];
        _maxa = max(a[i], _maxa);
        while(ma[back] <= _maxa && max(lim, i - k) <= back)
        {
            ma[back] = a[i];
            update(back, mxdp[back] + a[i]);
            if(ma[back - 1] <= _maxa && max(lim, i - k) <= back - 1) back--;
            else break;
        }
        if(max(lim, i - k) > back)
        {
            update(back + 1, mxdp[back + 1] + (ma[back + 1] = _maxa));
            back++;
        }
        dp[i] = suffixAsk(max(lim, i - k));
        if(i % k == 0)
        {
            int max2 = 0;
            for(int j = i; j >= max(day[today], i - k); j--)
            {
                //ma[j] = max(ma[j + 1], a[j]);
                //update(j, dp[j] + ma[j + 1]);
                update(j, dp[j] + (ma[j] = max2));
                max2 = max(max2, a[j]);
                mxdp[j] = max(mxdp[j + 1], dp[j]);
            }
            today++;
            back = i;
            _maxa = 0;
        }
    }
    cout << dp[n] << endl;
}