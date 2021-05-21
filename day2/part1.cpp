#include <stdio.h>
#include <algorithm>

#define ull unsigned long long

int main(){

  ull n1, n2, n3, result = 0;

  while(scanf("%llux%llux%llu", &n1, &n2, &n3) != EOF){
  
    result += (2 * n1 * n2) + (2 * n1 * n3) + (2 * n2 * n3) + std::min(std::min(n1 * n2, n1 * n3), n2 * n3);

  }

  printf("%lld\n", result);

  return 0;
}

