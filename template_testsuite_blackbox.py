import unittest
from typing import Tuple, List, Dict, Union
from enum import Enum


### Part 1 of the assignment ###
# Look for the triple question marks. They indicate the locations in this file where there are questions awaiting your answers.

def count_active_contributors(number_of_repos, number_of_commits):
    """
    Counts the number of contributors who have more than the specified number of repositories and commits.

    Args:
        number_of_repos (int): Minimum number of repositories a contributor must exceed to be counted.
                              Valid range: 1 <= number_of_repos <= 100
        number_of_commits (int): Minimum number of commits a contributor must exceed to be counted.
                                Valid range: 1 <= number_of_commits < 1000

    Returns:
        int: The count of contributors who exceed both the specified number of repositories and the specified number of commits.
    """
    pass


def compute_ranking(number_of_months, num_contributors):
    """
    Computes a ranking of contributors based on their commit activity.

    Args:
        number_of_months (int): The time range in months to consider when counting commits.
                               Valid range: 1 <= number_of_months <= 24
        num_contributors (int): The length of the contributor list to be returned.
                              Valid range: 2 <= num_contributors <= 100

    Returns:
        list: A list of length `num_contributors` of the top contributors, ordered by descending number of commits.

    """
    pass


class Scope(Enum):
    REPOSITORY = "repository"
    ORGANIZATION = "organization"


class Metric(Enum):
    COMMITS = "commits"
    PULL_REQUESTS = "pull_requests"
    ISSUES = "issues"
    COMPOSITE = "composite"


class TimeGranularity(Enum):
    DAY = "day"
    WEEK = "week"
    MONTH = "month"
    QUARTER = "quarter"
    YEAR = "year"


def score_contributors(time_granularity: TimeGranularity, scope: Scope, metric: Metric):
    """
    Scores contributors based on their activity in a given time period, scope, and metric.

    Args:
        time_granularity (TimeGranularity): The time period granularity for calculating scores.
                                           Options: DAY, WEEK, MONTH, QUARTER, YEAR
        scope (Scope): The scope level at which to aggregate contribution data.
                      Options: REPOSITORY, ORGANIZATION
        metric (Metric): The specific activity metric used for scoring.
                        Options: COMMITS, PULL_REQUESTS, ISSUES, COMPOSITE

    Returns:
        dict: A dictionary mapping contributor names or IDs to their calculated scores
              based on the specified parameters.

    Notes:
        - When using COMPOSITE metric, scores are calculated using the other metrics.
    """
    pass


def are_stats_available(repo_name: str, user: str):
    """
    For this assignment, we use a simplified model of GitHub.
    An organization is either public or private.
    Each repository belongs to one organization.
    Users can be a member of an organization.

    Statistics are available for a repository only if:
    * The repository is accessible to the user, which requires:
    The repository to belongs to a public organization, or
    The repository belongs to a private organization that the user is a member of.
    * The repository is not empty (contains some data).

    If the repository is both accessible and not empty, the code returns True.
    If the repository is not accessible, the code will raise an NotAccessibleException.
    If the repository is accessible and empty, the code returns False.
    """
    pass


class TestScoreContributors(unittest.TestCase):
    def test_count_active_contributors(self):
        # Question 1: write a test suite for `count_active_contributors` using boundary value testing under the weak normal assumption.
        # Refer to the docstring of the `count_active_contributors` function, which can be found above.
        # In this assignment, we are less interested in the assertions, and more interested in the selection of input values
        #
        # e.g., each test case should be a call to the function:
        # count_active_contributors(1, 1)  # note that this example can be deleted from your answer

        # Boundary values for number_of_repos: 1, 50, 100
        # Boundary values for number_of_commits: 1, 500, 999

        # Test case 1: Minimum values for both parameters
        count_active_contributors(1, 1)

        # Test case 2: Minimum value for number_of_repos, middle value for number_of_commits
        count_active_contributors(1, 500)

        # Test case 3: Minimum value for number_of_repos, maximum value for number_of_commits
        count_active_contributors(1, 999)

        # Test case 4: Middle value for number_of_repos, minimum value for number_of_commits
        count_active_contributors(50, 1)

        # Test case 5: Middle values for both parameters
        count_active_contributors(50, 500)

        # Test case 6: Middle value for number_of_repos, maximum value for number_of_commits
        count_active_contributors(50, 999)

        # Test case 7: Maximum value for number_of_repos, minimum value for number_of_commits
        count_active_contributors(100, 1)

        # Test case 8: Maximum value for number_of_repos, middle value for number_of_commits
        count_active_contributors(100, 500)

        # Test case 9: Maximum values for both parameters
        count_active_contributors(100, 999)

    def test_compute_rankings(self):
        # Question 2: write a test suite for `compute_ranking` using boundary value testing under the strong robust assumption
        # Refer to the docstring of the `compute_ranking` function, which can be found above.
        # In this assignment, we are less interested in the assertions, and more interested in the selection of input values.
        # compute_ranking(1, 2)  # note that this example can be deleted from your answer

        # Boundary values for number_of_months: 0, 1, 12, 24, 25
        # Boundary values for num_contributors: 1, 2, 50, 100, 101

        # Test case 1: Minimum valid values for both parameters
        compute_ranking(1, 2)

        # Test case 2: Minimum valid value for number_of_months, middle valid value for num_contributors
        compute_ranking(1, 50)

        # Test case 3: Minimum valid value for number_of_months, maximum valid value for num_contributors
        compute_ranking(1, 100)

        # Test case 4: Middle valid value for number_of_months, minimum valid value for num_contributors
        compute_ranking(12, 2)

        # Test case 5: Middle valid values for both parameters
        compute_ranking(12, 50)

        # Test case 6: Middle valid value for number_of_months, maximum valid value for num_contributors
        compute_ranking(12, 100)

        # Test case 7: Maximum valid value for number_of_months, minimum valid value for num_contributors
        compute_ranking(24, 2)

        # Test case 8: Maximum valid value for number_of_months, middle valid value for num_contributors
        compute_ranking(24, 50)

        # Test case 9: Maximum valid values for both parameters
        compute_ranking(24, 100)

        # Test case 10: Invalid value for number_of_months (below minimum), valid value for num_contributors
        compute_ranking(0, 2)

        # Test case 11: Invalid value for number_of_months (above maximum), valid value for num_contributors
        compute_ranking(25, 2)

        # Test case 12: Valid value for number_of_months, invalid value for num_contributors (below minimum)
        compute_ranking(1, 1)

        # Test case 13: Valid value for number_of_months, invalid value for num_contributors (above maximum)
        compute_ranking(1, 101)

        # Test case 14: Invalid values for both parameters
        compute_ranking(0, 1)

        # Test case 15: Invalid values for both parameters (above maximum)
        compute_ranking(25, 101)

    def test_score_contributors(self):
        # Question 3: write a test suite for `score_contributors` following 2-way testing.
        # Refer to the docstring of the `score_contributors` function, which can be found above
        # In this assignment, we are less interested in the assertions, and more interested in the selection of input values.
        #
        # score_contributors(TimeGranularity.MONTH, Scope.REPOSITORY,
        #                    Metric.COMMITS)  # note that this example can be deleted from your answer

        # For 2-way testing, we need to test all possible pairs of parameter values.
        # time_granularity: DAY, WEEK, MONTH, QUARTER, YEAR (5 values)
        # scope: REPOSITORY, ORGANIZATION (2 values)
        # metric: COMMITS, PULL_REQUESTS, ISSUES, COMPOSITE (4 values)

        # Test all pairs of time_granularity and scope
        score_contributors(TimeGranularity.DAY, Scope.REPOSITORY, Metric.COMMITS)
        score_contributors(TimeGranularity.DAY, Scope.ORGANIZATION, Metric.COMMITS)
        score_contributors(TimeGranularity.WEEK, Scope.REPOSITORY, Metric.COMMITS)
        score_contributors(TimeGranularity.WEEK, Scope.ORGANIZATION, Metric.COMMITS)
        score_contributors(TimeGranularity.MONTH, Scope.REPOSITORY, Metric.COMMITS)
        score_contributors(TimeGranularity.MONTH, Scope.ORGANIZATION, Metric.COMMITS)
        score_contributors(TimeGranularity.QUARTER, Scope.REPOSITORY, Metric.COMMITS)
        score_contributors(TimeGranularity.QUARTER, Scope.ORGANIZATION, Metric.COMMITS)
        score_contributors(TimeGranularity.YEAR, Scope.REPOSITORY, Metric.COMMITS)
        score_contributors(TimeGranularity.YEAR, Scope.ORGANIZATION, Metric.COMMITS)

        # Test all pairs of time_granularity and metric
        score_contributors(TimeGranularity.DAY, Scope.REPOSITORY, Metric.PULL_REQUESTS)
        score_contributors(TimeGranularity.DAY, Scope.REPOSITORY, Metric.ISSUES)
        score_contributors(TimeGranularity.DAY, Scope.REPOSITORY, Metric.COMPOSITE)
        score_contributors(TimeGranularity.WEEK, Scope.REPOSITORY, Metric.PULL_REQUESTS)
        score_contributors(TimeGranularity.WEEK, Scope.REPOSITORY, Metric.ISSUES)
        score_contributors(TimeGranularity.WEEK, Scope.REPOSITORY, Metric.COMPOSITE)
        score_contributors(TimeGranularity.MONTH, Scope.REPOSITORY, Metric.PULL_REQUESTS)
        score_contributors(TimeGranularity.MONTH, Scope.REPOSITORY, Metric.ISSUES)
        score_contributors(TimeGranularity.MONTH, Scope.REPOSITORY, Metric.COMPOSITE)
        score_contributors(TimeGranularity.QUARTER, Scope.REPOSITORY, Metric.PULL_REQUESTS)
        score_contributors(TimeGranularity.QUARTER, Scope.REPOSITORY, Metric.ISSUES)
        score_contributors(TimeGranularity.QUARTER, Scope.REPOSITORY, Metric.COMPOSITE)
        score_contributors(TimeGranularity.YEAR, Scope.REPOSITORY, Metric.PULL_REQUESTS)
        score_contributors(TimeGranularity.YEAR, Scope.REPOSITORY, Metric.ISSUES)
        score_contributors(TimeGranularity.YEAR, Scope.REPOSITORY, Metric.COMPOSITE)

        # Test all pairs of scope and metric
        score_contributors(TimeGranularity.DAY, Scope.ORGANIZATION, Metric.PULL_REQUESTS)
        score_contributors(TimeGranularity.DAY, Scope.ORGANIZATION, Metric.ISSUES)
        score_contributors(TimeGranularity.DAY, Scope.ORGANIZATION, Metric.COMPOSITE)
        score_contributors(TimeGranularity.DAY, Scope.REPOSITORY, Metric.PULL_REQUESTS)
        score_contributors(TimeGranularity.DAY, Scope.REPOSITORY, Metric.ISSUES)
        score_contributors(TimeGranularity.DAY, Scope.REPOSITORY, Metric.COMPOSITE)

    def test_stats_available(self):
        # Question 4: For the function `are_stats_available`, write a decision table.
        # Question 4a. Write out the table in markdown
        #  ??? TODO
        # | Conditions                     | R1 | R2 | R3 | R4 |
        # |--------------------------------|----|----|----|----|
        # |                                |    |    |    |    |
        # |                                |    |    |    |    |
        # |                                |    |    |    |    |
        # |                                |    |    |    |    |
        #

        # Decision Table for are_stats_available:
        # | Conditions                                | R1 | R2 | R3 | R4 |
        # |-------------------------------------------|----|----|----|----|
        # | Repository belongs to public org          | T  | T  | F  | F  |
        # | User is member of private org             | -  | -  | T  | F  |
        # | Repository is not empty                   | T  | F  | T  | T  |
        # |-------------------------------------------|----|----|----|----|
        # | Output                                    | T  | F  | T  | E  |
        # |-------------------------------------------|----|----|----|----|
        # | T = True, F = False, E = Exception, - = Don't Care |

        # Question 4b. Then, write the test cases
        # Note: in the test cases, give names to the repos/users to indicate if they are private, public, empty, etc.
        # Note: If you notice any ambiguity, add a comment documenting your assumptions.
        #
        # After each test case, add a comment to indicate which column of the decision table
        # Example:
        # are_stats_available("public_org/nonempty_repo1",
        #                     "public_org_developer")  # R1  # note that this example can be deleted from your answer

        # Test case for R1: Repository belongs to public org, repository is not empty
        are_stats_available("public_org/nonempty_repo1", "any_user")  # R1

        # Test case for R2: Repository belongs to public org, repository is empty
        are_stats_available("public_org/empty_repo1", "any_user")  # R2

        # Test case for R3: Repository belongs to private org, user is member, repository is not empty
        are_stats_available("private_org/nonempty_repo1", "private_org_member")  # R3

        # Test case for R4: Repository belongs to private org, user is not member, repository is not empty
        are_stats_available("private_org/nonempty_repo1", "non_member_user")  # R4

# for this assignment, you do not have to execute the test cases in this file
# as such, you will not be penalized for test cases that do not compile, as long as the intent of each test case is clear.
# You can also assume that all test cases written will be executed, regardless of whether a test case results in an exception to be thrown
# i.e., you don't have to catch or handle exceptions
# for this assignment, assertions are optional
