#include <stdio.h>
#include <algorithm>

#define ull unsigned long long

int main(){

  ull n1, n2, n3, result = 0, vec[3];

  while(scanf("%lldx%lldx%lld", &n1, &n2, &n3) != EOF){

    vec[0] = n1, vec[1] = n2, vec[2] = n3;

    std::sort(vec, vec + 3);

    result += (2 * vec[0]) + (2 * vec[1]) + (vec[0] * vec[1] * vec[2]);

  }

  printf("%lld\n", result);

  return 0;
}
