import pytest

@pytest.fixture()
def launch_setup():
    print("SETUP for browser config")
    yield
    print("TEARDOWN for browser config")


class Test_TestSuite1:
    def test_case_1(self, launch_setup):
        print("this is test case 1")

    def test_case_2(self, launch_setup):
        print("this is test case 2")

    def test_case_3(self, launch_setup):
        print("this is test case 3")

    @pytest.mark.parametrize("name",["ram", "sam", "scott", "john"])
    def test_case_4(self, name):
        print("this is test case 4 ", name)

    @pytest.mark.parametrize("name,age", [("ram", "25"), ("sam", "30"), ("scott", "28")])
    def test_case_5(self, name, age):
        print("this is test case 5 ", name, age)


