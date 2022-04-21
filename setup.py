from setuptools import setup, find_packages
from functools import reduce

version="0.0.0"

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(name='phishpedia',
      version="0.0.0",
      description='Phishpedia',
      long_description=long_description,
      author='Ruofan Liu',
      author_email='liu.ruofan16@u.nus.edu',
      url='https://github.com/lindsey98/Phishpedia',
      license='Apache License 2.0',
      python_requires='==3.9.*',
      packages=['phishpedia', 'phishpedia.src', 'phishpedia.src.siamese_pedia',
                'phishpedia.src.detectron2_pedia', 'phishpedia.src.adv_attack',
                'phishpedia.src.util', 'phishpedia.src.siamese_pedia.siamese_retrain', 'phishpedia.src.siamese_pedia.siamese_retrain.bit_pytorch',
                'phishpedia.src.detectron2_pedia.configs', 'phishpedia.src.detectron2_pedia.detectron2_1',
                'phishpedia.src.detectron2_pedia.configs.bases',
                'phishpedia.src.adv_attack.attack'],
      install_requires=[
            'torchsummary',
            'scipy',
            'tldextract',
            'opencv-python',
            'selenium',
            'helium',
            'selenium-wire',
            'webdriver-manager',
            'pandas',
            'numpy',
            'tqdm',
            'Pillow',
            'pathlib',
            'fvcore',
            'pycocotools',
            'scikit-learn',
            'pyyaml'
      ],
      package_data={
            # If any package contains *.txt or *.rst files, include them:
            "": ["*.yaml", "*.pkl", "*.pth", "*.zip", "*.tar"],
      },
      include_package_data=True
      )
