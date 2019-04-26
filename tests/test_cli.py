import pytest
import cli


def test_number_of_arguments():

    # check if right amamount of arguements get passed
    assert cli.check_number_of_arguments([1, 2, 3]) is None
    assert cli.check_number_of_arguments([1, 2]) is None

    # check if too many Arugements lead to Assertion Error
    with pytest.raises(AssertionError):
        cli.check_number_of_arguments([1, 2, 3, 4])

    # check ot too less Arugements lead to Assertion Error
    with pytest.raises(AssertionError):
        cli.check_number_of_arguments([])
        cli.check_number_of_arguments([1])


def test_get_filenames_from_arguments():

    # check if filenames get parsed correctly
    file1, file2 = cli.get_filenames_from_arguments(['placeholder', 'bar.csv', 'foo.csv'])
    assert file1 == 'bar.csv' and file2 == 'foo.csv'

    # check if 'ads.csv' gets added automatically if no second arguemnt is given
    file1, file2 = cli.get_filenames_from_arguments(['placeholder', 'foo.csv'])
    assert file1 == 'foo.csv' and file2 == 'ads.csv'


def test_check_name():

    # check if exsiting file gets recogniced
    assert cli.check_name('data/keywords.csv') is None

    # check if FileNotFoundError gets catched
    with pytest.raises(SystemExit):
        cli.check_name('data/foo.csv')
        cli.check_name('asdf')


def test_check_csv_extension():

    # check if .csv gets added if not given
    assert cli.check_csv_extension('foo') == 'foo.csv'

    # checks if .csv does not get added a second time it already given
    assert cli.check_csv_extension('bar.csv') == 'bar.csv'
    assert cli.check_csv_extension('test.csv') != 'test.csv.csv'


def test_handle_input():

    # check if right file gets recogniced
    assert cli.handle_input(['placeholder', 'data/keywords.csv'])

    # check if FileNotFound gets catched
    with pytest.raises(SystemExit):
        cli.handle_input(['placeholder', 'data/foo.csv'])

    file1, file2 = cli.handle_input(['placeholder', 'data/keywords'])
    # check if .csv gets appended automatically
    assert file1 == 'data/keywords.csv'

    # check if ads.csv gets added automatically
    assert file2 == 'ads.csv'
