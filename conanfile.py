from conan import ConanFile
from conan.tools.cmake import CMakeToolchain, CMake, cmake_layout, CMakeDeps
from conan.tools.files import copy
import os

class JsidlXmlRecipe(ConanFile):
    name = "jsidl_xml"
    version = "0.0.1"
    package_type = "header-library"

    # Optional metadata
    license = "BSD-3-Clause"
    url = "github.com/FFI-no/jsidl_xml"

    # Binary configuration
    settings = "os", "compiler", "build_type", "arch"
    options = {}

    # Sources are located in the same place as this recipe, copy them to the recipe
    exports_sources = "LICENSE","CMakeLists.txt","urn.jaus.jss.core-v1.1/*", "urn.jaus.jss.environment_sensing/*", "urn.jaus.jss.manipulator/*", "urn.jaus.jss.mobility/*", "urn.jaus.jss.ugv/*"

    def layout(self):
        cmake_layout(self)
        self.cpp.package.resdirs = ["res"]


    def generate(self):
        tc = CMakeToolchain(self)
        tc.generate()


    def build(self):
        cmake = CMake(self)
        cmake.configure()
        cmake.install()


    def package(self):
        copy(self,"*.xml",src=self.source_folder,dst=os.path.join(self.package_folder, "res"))
        copy(self,"LICENSE",src=self.source_folder,dst=os.path.join(self.package_folder, "res"))

    def package_info(self):
        self.cpp_info.set_property("cmake_file_name", "jsidl_xml")
        self.cpp_info.set_property("cmake_target_name","jsidl_xml::jsidl_xml")
        self.cpp_info.resdirs = ["res"]
