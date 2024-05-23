"""A setuptools based setup module.

See:
https://packaging.python.org/en/latest/distributing.html
https://github.com/pypa/sampleproject
"""

# Allow editable install into user site directory.
# See https://github.com/pypa/pip/issues/7953.
import site
import sys
site.ENABLE_USER_SITE = '--user' in sys.argv[1:]

# To use a consistent encoding
from codecs import open
# Always prefer setuptools over distutils
from distutils.core import setup
from os import path

# import numpy
from setuptools import find_packages
# from Cython.Build import cythonize

here = path.abspath(path.dirname(__file__))

# dependencies only required during test
test = [
    'pytest',
    'pytest-cov',
]

# Get the long description from the relevant file
try:
    with open(path.join(here, 'README.md'), encoding='utf-8') as f:
        long_description = f.read()
except FileNotFoundError:
    long_description = ''

setup(
    name='tssep_data',

    # Versions should comply with PEP440.  For a discussion on single-sourcing
    # the version across setup.py and the project code, see
    # https://packaging.python.org/en/latest/single_source_version.html
    version='0.0.0',

    description='TS-SEP: Joint Diarization and Separation Conditioned on Estimated Speaker Embeddings',
    long_description=long_description,

    # Denotes that our long_description is in Markdown; valid values are
    # text/plain, text/x-rst, and text/markdown
    #
    # Optional if long_description is written in reStructuredText (rst) but
    # required for plain-text or Markdown; if unspecified, "applications should
    # attempt to render [the long_description] as text/x-rst; charset=UTF-8 and
    # fall back to text/plain if it is not valid rst" (see link below)
    #
    # This field corresponds to the "Description-Content-Type" metadata field:
    # https://packaging.python.org/specifications/core-metadata/#description-content-type-optional
    long_description_content_type='text/markdown',  # Optional (see note above)

    # The project's main homepage.
    # url='https://github.com/...',

    # Author details
    author='Christoph Boeddeker',
    # author_email='...',

    # Choose your license
    # license='MIT',

    # See https://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        # How mature is this project? Common values are
        #   3 - Alpha
        #   4 - Beta
        #   5 - Production/Stable
        'Development Status :: 3 - Alpha',

        # Indicate who your project is intended for
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',

        # Pick your license as you wish (should match "license" above)
        'License :: OSI Approved :: MIT License',

        # Specify the Python versions you support here. In particular, ensure
        # that you indicate whether you support Python 2, Python 3 or both.
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],

    # What does your project relate to?
    keywords='audio speech',

    # You can just specify the packages manually here if your project is
    # simple. Or you can use find_packages().
    packages=find_packages(exclude=['contrib', 'docs', 'tests*']),

    # List run-time dependencies here.  These will be installed by pip when
    # your project is installed. For an analysis of "install_requires" vs pip's
    # requirements files see:
    # https://packaging.python.org/en/latest/requirements.html
    install_requires=[
        'numpy',
        'scipy',
        'Cython',
        'IPython',
        'tensorboardX',
        'webrtcvad',  # LibriCSS dependency
        'resampy',  # LibriCSS dependency
        "dataclasses; python_version<'3.7'",  # dataclasses is in py37 buildin
        'soundfile',
        'einops',
        'cached_property',
        'lazy_dataset',
        'diskcache',  # Optional lazy_dataset dependency
        'humanfriendly',  # Optional lazy_dataset dependency
        'nara_wpe',
        'kaldi_io',
        'fire',
        'sacred',
        'tqdm',
        'dlp_mpi @ git+http://github.com/fgnt/dlp_mpi',  # Make a release and remove git+
        'editdistance',
        'natsort',
        'meeteval @ git+http://github.com/fgnt/meeteval',  # Make a release and remove git+
        'openai-whisper',
        'psutil',
        'pyroomacoustics',
    	'pytimeparse',
        'questionary',
        'pyyaml>=5.1',
        'simplejson',
        'torch',
        'torchvision',
        'torchaudio',
        'paderbox @ git+http://github.com/fgnt/paderbox',  # Has the pypi version all required features?
        'padertorch @ git+http://github.com/fgnt/padertorch',  # Has the pypi version all required features?
        'pb_bss @ git+http://github.com/fgnt/pb_bss',
        'rirgen @ git+https://github.com/boeddeker/rirgen',
        'sms_wsj @ git+https://github.com/fgnt/sms_wsj',
        'mms_msg @ git+https://github.com/fgnt/mms_msg',
        'espnet',
        # 'espnet_model_zoo',
        # 'nemo_toolkit[all]',
    ],

    # Installation problems in a clean, new environment:
    # 1. `cython` and `scipy` must be installed manually before using
    # `pip install`

    # List additional groups of dependencies here (e.g. development
    # dependencies). You can install these using the following syntax,
    # for example:
    # $ pip install -e .[all]
    extras_require={
        'all': test,
    },

    # ext_modules=cythonize([
    #     '...',
    # ],
    #     annotate=True,
    # ),
    # include_dirs=[numpy.get_include()],
    # entry_points={
    #     "console_scripts": [
    #         '...',
    #     ]
    # },
)
