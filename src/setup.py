from setuptools import setup
import setup_translate

pkg = 'SystemPlugins.TransCodingSetup'
setup(name='enigma2-plugin-systemplugins-transcodingsetup',
       version='3.0',
       description='Setup transcoding of your VU+',
       package_dir={pkg: 'TransCodingSetup'},
       packages=[pkg],
       package_data={pkg: ['images/*.png', '*.png', '*.xml', 'locale/*/LC_MESSAGES/*.mo', 'setup.xml', 'plugin.png']},
       cmdclass=setup_translate.cmdclass,  # for translation
      )
