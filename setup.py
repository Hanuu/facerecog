import setuptools
setuptools.setup(
    name="GoPiGo",
    description="Drivers and examples for using the GoPiGo in Python",
    author="Dexter Industries",
    url="http://www.dexterindustries.com/GoPiGo/",
    py_modules=['I2C_mutex','gopigo','easygopigo','line_follower.line_sensor', 'line_follower.scratch_line'],
    install_requires=open('requirements.txt').readlines(),
)