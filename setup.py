#!/usr/bin/env python

from __future__ import division, print_function

import os.path
import numpy

from setuptools import Extension, setup
from BioExt.references._factory import _installrefdirs

np_inc = [os.path.join(os.path.dirname(numpy.__file__), 'core', 'include')]

ext_modules = [
    Extension(
        'BioExt.align._align',
        sources=[
            os.path.join('BioExt', 'align', '_align.c'),
            os.path.join('BioExt', 'align', 'alignment.c')
            ],
        include_dirs=np_inc,
        libraries=['m'],
        extra_compile_args=['-O3', '-I.']
        ),
    Extension(
        'BioExt.merge._merge',
        sources=[
            os.path.join('BioExt', 'merge', '_merge.c'),
            os.path.join('BioExt', 'merge', 'merge.cpp')
            ],
        extra_compile_args=['-O3', '-I.']
        ),
    Extension(
        'BioExt.rateclass._rateclass',
        sources=[
            os.path.join('BioExt', 'rateclass', '_rateclass.cpp'),
            os.path.join('BioExt', 'rateclass', 'rateclass.cpp')
            ],
        extra_compile_args=['-O3', '-I.']
        )
    ]


setup(
    name='biopython-extensions',
    version='0.18.5',
    description='Misc utilities and definitions not included or hidden in BioPython',
    author='N Lance Hepler',
    author_email='nlhepler@gmail.com',
    url='http://github.com/veg/bioext',
    license='GNU GPL version 3',
    packages=[
        'BioExt',
        'BioExt.align',
        'BioExt.args',
        'BioExt.collections',
        'BioExt.errorize',
        'BioExt.freetype',
        'BioExt.freetype.ft_enums',
        'BioExt.io',
        'BioExt.io.BamIO',
        'BioExt.io.LazyAlignIO',
        'BioExt.io.SamIO',
        'BioExt.joblib',
        'BioExt.joblib.test',
        'BioExt.merge',
        'BioExt.misc',
        'BioExt.ndarray',
        'BioExt.optimize',
        'BioExt.orflist',
        'BioExt.phylo',
        'BioExt.quiver',
        'BioExt.rateclass',
        'BioExt.references',
        'BioExt.scorematrices',
        'BioExt.stats',
        'BioExt.uds',
        'BioExt.untranslate'
        ],
    package_dir={
        'BioExt': 'BioExt',
        'BioExt.align': 'BioExt/align',
        'BioExt.args': 'BioExt/args',
        'BioExt.collections': 'BioExt/collections',
        'BioExt.errorize': 'BioExt/errorize',
        'BioExt.freetype': 'BioExt/freetype',
        'BioExt.freetype.ft_enums': 'BioExt/freetype/ft_enums',
        'BioExt.io': 'BioExt/io',
        'BioExt.io.BamIO': 'BioExt/io/BamIO',
        'BioExt.io.LazyAlignIO': 'BioExt/io/LazyAlignIO',
        'BioExt.io.SamIO': 'BioExt/io/SamIO',
        'BioExt.joblib': 'BioExt/joblib',
        'BioExt.joblib.test': 'BioExt/joblib/test',
        'BioExt.merge': 'BioExt/merge',
        'BioExt.misc': 'BioExt/misc',
        'BioExt.ndarray': 'BioExt/ndarray',
        'BioExt.optimize': 'BioExt/optimize',
        'BioExt.orflist': 'BioExt/orflist',
        'BioExt.phylo': 'BioExt/phylo',
        'BioExt.quiver': 'BioExt/quiver',
        'BioExt.rateclass': 'BioExt/rateclass',
        'BioExt.references': 'BioExt/references',
        'BioExt.scorematrices': 'BioExt/scorematrices',
        'BioExt.stats': 'BioExt/stats',
        'BioExt.uds': 'BioExt/uds',
        'BioExt.untranslate': 'BioExt/untranslate'
        },
    package_data={
        'BioExt': [
            'data/fonts/ttf/*.ttf',
            'data/scorematrices/*.txt'
            ] + _installrefdirs
        },
    scripts=[
        'scripts/bam2fna',
        'scripts/bam2msa',
        'scripts/bamclip',
        'scripts/bealign',
        'scripts/clipedge',
        'scripts/consensus',
        'scripts/msa2bam',
        'scripts/seqmerge',
        'scripts/translate'
        # 'scripts/variants'
        ],
    ext_modules=ext_modules,
    install_requires=[
        'biopython >=1.58',
        'numpy >=1.6',
        'scipy >=0.15',
        'pysam==0.8.4'
        ]
    )
