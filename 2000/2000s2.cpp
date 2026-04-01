#include <bits/stdc++.h>
using namespace std;

int main() {
    int n;
    cin >> n;

    vector<double> streams(n);
    for (int i = 0; i < n; ++i) {
        cin >> streams[i];
    }

    while (true) {
        int cmd;
        cin >> cmd;

        if (cmd == 77) break;                  // end
        else if (cmd == 99) {                  // split
            int idx, p;
            cin >> idx >> p;                   // 1-based index, percentage to left
            idx -= 1;                             // convert to 0-based
            double flow = streams[idx];
            double left = flow * p / 100.0;
            double right = flow - left;

            // Replace stream[idx] with left, and insert right after it
            streams[idx] = left;
            streams.insert(streams.begin() + idx + 1, right);
        } else if (cmd == 88) {                // join
            int idx;
            cin >> idx;                        // 1-based index of left stream (join with immediate right)
            idx -= 1;                             // convert to 0-based
            if (idx >= 0 && idx + 1 < (int)streams.size()) {
                streams[idx] += streams[idx + 1];
                streams.erase(streams.begin() + idx + 1);
            }
        }
    }

    // Output final flows rounded to nearest integer, space-separated
    for (size_t i = 0; i < streams.size(); ++i) {
        if (i) cout << ' ';
        cout << (long long)llround(streams[i]);
    }
    cout << '\n';
    return 0;
}
