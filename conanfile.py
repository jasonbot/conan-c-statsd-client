from conans import ConanFile, CMake, tools
import os


class StatsdclientConan(ConanFile):
    name = "statsd-client"
    version = "1.0.0"
    license = "MIT"
    url = "https://github.com/romanbsd/statsd-c-client"
    settings = "os", "compiler", "build_type", "arch"
    options = {"shared": [True, False]}
    default_options = "shared=False"

    def source(self):
        self.run("git clone git@github.com:romanbsd/statsd-c-client.git")

    def build(self):
        self.run("cd statsd-c-client && make lib")

    def package(self):
        self.copy("*.h", dst="include", src="statsd-c-client")
        self.copy("*hello.lib", dst="lib", src="statsd-c-client", keep_path=False)
        self.copy("*.dll", dst="bin", src="statsd-c-client", keep_path=False)
        self.copy("*.so", dst="lib", src="statsd-c-client", keep_path=False)
        self.copy("*.a", dst="lib", src="statsd-c-client", keep_path=False)
