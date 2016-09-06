#include "openjpeg-2.1/opj_config.h"
#include <iostream>       // std::cout
#include <string>         // std::string

int main(){
  int major(OPJ_VERSION_MAJOR);
  int minor(OPJ_VERSION_MAJOR);
  int build(OPJ_VERSION_MAJOR);

  // different member versions of find in the same order as above:
  if (major!=2)
    std::cout << "major = " << major << std::endl;
    return 0;
  if (minor!=1)
    std::cout << "minor = " << minor << std::endl;
    return 0;
  if (build!=1)
    std::cout << "build = " << build << std::endl;
    return 0;
  return 1;
}
