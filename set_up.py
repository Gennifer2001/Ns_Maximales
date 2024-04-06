import setuptools

with open("DESCRIPTION.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name='NsMaximales',
    version='0.1.0',
    author="Yeimi Rodriguez y Genifer Montaño",
    author_email="gennifermontanorodriguez@gmail.com o yeimir0000@gmail.com",
    description="NsMaximales se encarga de calcular los n-subárboles maximales y apartir de ellos obtener una base topológica",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/institutohumai/humai_utils',
    license='MIT',
    packages=['Ns_Maximales'],
    install_requires=["ete3","pandas","scipy","numpy"],
    CLASSIFIERS = ['Development Status :: 4 - Beta',
                                 'Intended Audience :: Developers',
                                 'Intended Audience :: Data Analysts',
                                 'License :: OSI Approved :: MIT License',
                                 'Natural Languaje :: Spanish',
                                 'Operating System :: Microsoft :: Windows',
                                 'Programming Language :: Python',
                                 'Topic :: Data Analytics',
                                 'Topic :: Topology']
)
