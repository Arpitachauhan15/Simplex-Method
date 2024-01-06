#include <iostream>
#include <iomanip>
#include <cmath>
using namespace std;

void init(float x[], int n)
{
    for (int i = 0; i < n; i++)
        x[i] = 0;
}

int main()
{
    int numVariables, numConstraints;

    cout << "Enter the number of variables: ";
    cin >> numVariables;

    cout << "Enter the number of constraints: ";
    cin >> numConstraints;

    const int ND = numVariables;
    const int NS = numConstraints;
    const int N = ND + NS;

    float a[NS][N + 1], c[N], cb[NS], th[NS];
    float x[ND], cj, z, t, b, min, max;

    init(c, N);
    init(cb, NS);
    init(th, NS);
    init(x, ND);

    for (int i = 0; i < NS; i++)
        init(a[i], N + 1);
    
    for (int i = 0; i < NS; i++)
        a[i][i + ND] = 1.0;

    int bas[NS];
    for (int i = 0; i < NS; i++)
        bas[i] = ND + i;

    cout << "Enter the constraints" << endl;
    for (int i = 0; i < NS; i++)
    {
        cout << "Enter coefficients for constraint " << (i + 1) << ": ";
        for (int j = 0; j < ND; j++)
            cin >> a[i][j];
        cout << "Enter the right-hand side value: ";
        cin >> a[i][N];
    }

    cout << "Enter the objective function coefficients" << endl;
    for (int j = 0; j < ND; j++)
        cin >> c[j];

    cout << fixed;
    while (1)
    {
        max = 0;
        int kj = 0;

        for (int j = 0; j < N; j++)
        {
            z = 0;
            for (int i = 0; i < NS; i++)
                z += cb[i] * a[i][j];
            cj = c[j] - z;
            if (cj > max)
            {
                max = cj;
                kj = j;
            }
        }

        if (max <= 0)
            break;

        max = 0;

        for (int i = 0; i < NS; i++)
        {
            if (a[i][kj] != 0)
            {
                th[i] = a[i][N] / a[i][kj];
                if (th[i] > max)
                    max = th[i];
            }
        }

        if (max <= 0)
        {
            cout << "Unbounded solution";
            return 1;
        }

        min = max;
        int ki = 0;

        for (int i = 0; i < NS; i++)
        {
            if ((th[i] < min) && (th[i] != 0))
            {
                min = th[i];
                ki = i;
            }
        }

        t = a[ki][kj];

        for (int j = 0; j < N + 1; j++)
            a[ki][j] /= t;

        for (int i = 0; i < NS; i++)
        {
            if (i != ki)
            {
                b = a[i][kj];
                for (int k = 0; k < N + 1; k++)
                    a[i][k] -= a[ki][k] * b;
            }
        }

        cb[ki] = c[kj];
        bas[ki] = kj;
    }

    for (int i = 0; i < NS; i++)
    {
        if ((bas[i] >= 0) && (bas[i] < ND))
            x[bas[i]] = a[i][N];
    }

    z = 0;

    for (int i = 0; i < ND; i++)
    {
        z += c[i] * x[i];
        cout << "x[" << setw(3) << i + 1 << "]=" << setw(7) << setprecision(2) << x[i] << endl;
    }

    cout << "Optimal value=" << setw(7) << setprecision(2) << z << endl;
     return 0;
}
