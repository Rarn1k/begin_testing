import pytest

cnt = 0

@pytest.fixture(autouse=True)
def clean_text_file():
    global cnt
    with open("tests/test_file_workers/testfile.txt", "w"):
        pass
    cnt += 1
    print(cnt)
