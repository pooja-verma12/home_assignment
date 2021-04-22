import pytest
import google_drive
import os.path,time

# Test object for the class DriveAPI
test_obj = google_drive.DriveAPI()

@pytest.mark.parametrize("f_id", ["16guerC4AJSVghfm4q6Wvw-AxpRw5yTia"])
@pytest.mark.parametrize("f_name", ["Pooja_Verma.pdf"])
def test_case_1(f_id,f_name):

	'''TC-1: Verifies that a file with valid "file name" and valid "file id"
	is successfully downloaded'''

	# Initialize the expected value to True
	exp_success = True

	# Capture the actual value from the method's return
	act_success = test_obj.FileDownload(f_id, f_name)

	# Compare actual value with expected
	assert act_success == exp_success


@pytest.mark.parametrize("f_id", ["16guerC4AJSVghfm4q6Wvw-AxpRw5yTia"])
@pytest.mark.parametrize("f_name", ["xxx.pdf"])
def test_case_2(f_id,f_name):

	'''TC-2: Verifies that a file with invalid "file name" and valid "file id"
	is successfully downloaded'''

	# Initialize the expected value to True
	exp_success = True

	# Capture the actual value from the method's return
	act_success = test_obj.FileDownload(f_id, f_name)

	# Compare actual value with expected
	assert act_success == exp_success


@pytest.mark.parametrize("f_id", ["xxx"])
@pytest.mark.parametrize("f_name", ["xxx.pdf"])
def test_case_3(f_id,f_name):

	'''TC-3: Verifies that a file with invalid "file name" and invalid "file id"
	is not downloaded'''

	# Initialize the expected value to False
	exp_success = False

	# Capture the actual value from the method's return
	act_success = test_obj.FileDownload(f_id, f_name)

	# Compare actual value with expected
	assert act_success == exp_success


@pytest.mark.parametrize("f_id", ["16guerC4AJSVghfm4q6Wvw-AxpRw5yTia"])
@pytest.mark.parametrize("f_name", ["Pooja_Verma.pdf"])
def test_case_4(f_id,f_name):

	'''TC-4: Verifies that a file will be downloaded again even if it
	already exsists to ensure latest/updated files are fetched'''

	# Invoke the method to download the file
	test_obj.FileDownload(f_id, f_name)

	# Initialize the expected value
	exp_time = time.ctime(os.path.getmtime(f_name))

	# Invoke the method to download the file again
	test_obj.FileDownload(f_id, f_name)

	# Capture expected value
	act_time = time.ctime(os.path.getmtime(f_name))

	# Compare actual value with expected
	assert exp_time < act_time


@pytest.mark.parametrize("f_id", ["1sJ9c0AwRShRkpdoy6FjjvhfH3x3XfDTl"])
@pytest.mark.parametrize("f_name", ["test_folder"])
def test_case_5(f_id,f_name):

	'''TC-5: Verifies that a folder(containing some files) cannot be downloaded
	when folder name is provided as file name'''

	# Initialize the expected value to True
	exp_success = False

	# Capture the actual value from the method's return
	act_success = test_obj.FileDownload(f_id, f_name)

	# Compare actual value with expected
	assert act_success == exp_success

@pytest.mark.parametrize("f_id", ["1yFtwvX6RS-Z1X2POr5_Rv9gdqXl3O5G6"])
@pytest.mark.parametrize("f_name", ["AJAY3808.JPG"])
def test_case_6(f_id,f_name):

	'''TC-6: Verifies that different file formats can be downloaded '''

	# Initialize the expected value to True
	exp_success = True

	# Capture the actual value from the method's return
	act_success = test_obj.FileDownload(f_id, f_name)

	# Compare actual value with expected
	assert act_success == exp_success


@pytest.mark.parametrize("f_id", ["1yFtwvX6RS-Z1X2POr5_Rv9gdqXl3O5G6", "1cU9CWVg_Ah6bX0bLFBK_1Tho1WHQj4wn"])
@pytest.mark.parametrize("f_name", ["AJAY3808.JPG", "Pooja_Verma.pdf"])
def test_case_7(f_id,f_name):

	'''TC-7: Verifies that multiple files can be downloaded '''

	# Initialize the expected value to True
	exp_success = True

	# Capture the actual value from the method's return
	act_success = test_obj.FileDownload(f_id, f_name)

	# Compare actual value with expected
	assert act_success == exp_success



























































































































































