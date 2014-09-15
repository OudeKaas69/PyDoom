#!python3

from distutils.core import setup
from distutils.extension import Extension
from Cython.Build import cythonize

setup (
    name = 'PyDoom rendering module',
    ext_modules = cythonize (
        Extension (
            "video",
            ["extsrc/video.pyx", "extsrc/video_cpp.cpp"],
            include_dirs = [
                "extern/SDL2-2.0.3/include",
                "extern/glew-1.11.0/include"
                ],
            libraries = [
                "opengl32",
                "extern/glew-1.11.0/lib/Release/Win32/glew32",
                "extern/SDL2-2.0.3/lib/SDL2"
                ]
            )
        ),
    )