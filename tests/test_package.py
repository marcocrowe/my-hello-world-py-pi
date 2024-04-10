"""
Test cases for the packages of the project
Copyright © 2024 Mark Crowe <https://github.com/marcocrowe>. All rights reserved.
"""

import unittest
import importlib.metadata as metadata


class TestPackage(unittest.TestCase):
    """
    Test case for the package.
    """

    def test_package(self) -> None:
        """
        Test if the hello-package module exists.
        """
        package_name: str = "hello-world"

        is_package_installed: bool = self.is_package_installed(package_name)

        self.assertTrue(is_package_installed)

    @staticmethod
    def is_package_installed(package_name: str) -> bool:
        """Test if the package is installed and
        prints the files in the distribution if it is installed.

        Args:
            package_name (str): The name of the package.

        Returns:
            bool: True if the package is installed, False otherwise.
        """
        try:
            distribution = metadata.distribution(package_name)
            print(f"\nFiles in the '{package_name}' distribution:\n")
            for package_path in distribution.files:
                print(package_path)
            return True
        except metadata.PackageNotFoundError:
            print(f"The '{package_name}' distribution is not installed.")
            return False


if __name__ == "__main__":
    unittest.main()
