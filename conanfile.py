from conan import ConanFile
from conan.tools.cmake import CMake, cmake_layout

class MjsTraderConan(ConanFile):
    name = "mjs_trader"
    version = "0.1"
    settings = "os", "compiler", "build_type", "arch"
    generators = "CMakeDeps", "CMakeToolchain"
    exports_sources = "CMakeLists.txt", "src/*", "include/*"

    def layout(self):
        cmake_layout(self)

    def build(self):
        cmake = CMake(self)
        cmake.configure()
        cmake.build()
    
    def requirements(self):
        self.requires("gtest/1.14.0")
        self.requires("fmt/10.2.1")

    # def build_requirements(self):
    #     self.tool_requires("cmake/3.22.6")
