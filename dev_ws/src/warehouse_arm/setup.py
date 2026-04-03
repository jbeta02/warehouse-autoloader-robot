from setuptools import find_packages, setup
from glob import glob
import os

package_name = 'warehouse_arm'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        # install launch files
        (os.path.join('share', 'warehouse_arm', 'launch'), glob('launch/*.launch.py')),

        # install URDF files
        (os.path.join('share', 'warehouse_arm', 'description'), glob('description/*.urdf')),
        (os.path.join('share','warehouse_arm','config'), glob('config/*')),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='jbeta',
    maintainer_email='jbeta02@gmail.com',
    description='TODO: Package description',
    license='TODO: License declaration',
    extras_require={
        'test': [
            'pytest',
        ],
    },
    entry_points={
        'console_scripts': [
            'move_arm = warehouse_arm.PandaMove:main',
        ],
    },
)
