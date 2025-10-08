#include <iostream>
#include <vector>
#include <algorithm>

using Matrix = std::vector<std::vector<double>>;
const std::size_t M = 4;
const std::size_t N = 4;

void printMatr(const Matrix& matr)
{
    for(const auto& i : matr)
    {
        for(const auto& j : i)
        {
            std::cout << j << " ";
        }
        std::cout << '\n';
    }
}

void printVec(const std::vector<double>& vec)
{
    for(const auto& i : vec)
    {
        std::cout << i << " ";

    }
    std::cout << '\n';
}

std::size_t ArgMax(const Matrix& matr, std::size_t i)
{
    double MAX = std::abs(matr[i][i]);
    std::size_t max_index = i;

    for (std::size_t j = i + 1; j < matr.size(); ++j)
    {
        if (std::abs(matr[j][i]) > MAX)
        {
            MAX = std::abs(matr[j][i]);
            max_index = j;
        }
    }
    return max_index;
}

void swapRows(Matrix& matr, std::size_t i, std::size_t j)
{
    for(std::size_t k = 0; k < matr.size(); ++k)
    {
        std::swap(matr[i][k], matr[j][k]);
    }
}


double dot(const std::vector<double>& a, const std::vector<double>& b)
{
    double sum = 0;
    for(std::size_t i = 0; i < a.size(); ++i)
    {
        sum += a[i] * b[i];
    }
    return sum;
}

void GaussMethod(Matrix& A, std::vector<double>& b)
{
    for(std::size_t i = 0; i < A.size() - 1; ++i)
    {
        std::size_t K = ArgMax(A, i);
        swapRows(A, i, K);
        std::swap(b[i], b[K]);
        for(std::size_t j = i + 1; j < A.size(); ++j)
        {
            double factor = A[j][i] / A[i][i];
            for(std::size_t k = 0; k < A.size(); ++k)
            {
                A[j][k] -= factor * A[i][k];
            }
            b[j] -= factor * b[i];
        }
    }
    
    //solution
    std::vector<double> sol(b.size(), 0);
    for(int i = A.size() - 1; i >=0; --i)
    {
        double npdot = dot(A[i], sol);
        
        sol[i] = (b[i] - npdot) / A[i][i];
    }
    std::cout << "Solution: ";
    printVec(sol);
    
}


int main()
{
    Matrix A = {
        {-3,3,1},
        {0,4,-2},
        {-3, 1, 5}
    };
    std::vector<double> B = {-2,5,1};
    GaussMethod(A, B);
}
