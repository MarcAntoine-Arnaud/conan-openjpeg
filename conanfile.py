from conans import ConanFile, CMake

class OpenJpegConan(ConanFile):
    name = "openjpeg"
    version = "2.1.1"
    generators = "cmake"
    settings = "os", "compiler", "build_type", "arch"
    exports = "*"
    url="https://github.com/MarcAntoine-Arnaud/conan-openjpeg"
    license="https://github.com/uclouvain/openjpeg/blob/master/LICENSE"

    def source(self):
        self.run("git clone git@github.com:uclouvain/openjpeg.git")

    def build(self):
        cmake = CMake(self.settings)
        self.run('cmake %s %s' % (self.conanfile_directory, cmake.command_line))
        self.run("cmake --build . %s" % cmake.build_config)

    def package(self):
        self.copy("*.h", dst="include")
        self.copy("*.lib", dst="lib", src="lib")
        self.copy("*.a", dst="lib", src="lib")

    def package_info(self):
        self.cpp_info.libs = ["openjp2"]

