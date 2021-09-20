ABIDE_SUBJECT_FETCHED = (
    "Successfully processed subject {subject_id} from site {site_name}"
)
ABIDE_TEMPORAL_WARNING = "WARNING: Error deleting temporal files: {message}"
BIDS_LABEL_MISSING = (
    "Participant label(s) not found in the BIDS root directory: {label}"
)
BIDS_GROUP_SIZE = (
    "Group size should be at least 0 (i.e. all participants assigned to same group)."
)
CLF_CAPTURED_WARNING = "Captured warning ({category}): {message}"
CLF_CLASSIFIER_MISSING = (
    "No training samples were given, and the --load-classifier option {info}."
)
CLF_SAVED_RESULTS = "Results saved as {path}."
CLF_TRAIN_LOAD_ERROR = "Errors ({n_errors}) loading training set: {errors}."
CLF_WRONG_PARAMETER_COUNT = "Wrong number of parameters."
DFCHECK_CSV_CHANGED = "Output CSV file changed one or more values."
DFCHECK_CSV_COLUMNS = "Output CSV file changed number of columns."
DFCHECK_DIFFERENT_BITS = "Dataset has different BIDS bits w.r.t. reference."
DFCHECK_DIFFERENT_LENGTH = "Input datases have different lengths (input={len_input}, reference={len_reference})."
DFCHECK_IQMS_CORRELATED = "All IQMs show a Pearson correlation >= 0.95."
DFCHECK_IQMS_UNDER_095 = "IQMs with Pearson correlation < 0.95:\n{iqms}"
HASH_REPORT = "{sha} {file_name}"
PLOT_REPORT_VERSION = "mriqc version:\t{version}"
PLOT_WORK_MISSING = "Work directory of a previous MRIQC run was not found."
SUBJECT_WRANGLER_DESCRIPTION = """\
BIDS-Apps participants wrangler tool
------------------------------------

This command arranges the participant labels in groups for computation, and checks that the \
requested participants have the corresponding folder in the bids_dir.\
"""
WEBAPI_GET = "Sending GET to {address}."
WEBAPI_REPORT = "There are {n_records} records in database."