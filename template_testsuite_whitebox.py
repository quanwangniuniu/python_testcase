import datetime
import unittest
from typing import Tuple, List, Dict, Union
from collections import defaultdict

from enum import Enum


### Part 2 of the assignment ###
# Look for the triple question marks. They indicate the locations in this file where there are questions awaiting your answers.
# First, look for Question 1, then continue to Question 2, then Question 3.


class Metric(Enum):
    COMMITS = "commits"
    PULL_REQUESTS = "pull_requests"
    ISSUES = "issues"
    # note that in testsuite_whitebox.py, we removed the `composite` enum. This is deliberate.


def compute_composite_score(dev_metrics: Dict[str, Dict[Metric, float]], aggregate_by: str) -> Dict[str, float]:
    """
    Compute a composite score for each developer based on their metrics.

    Args:
        dev_metrics: Dictionary mapping developer IDs to their metrics.
            Format: {"dev_id": {Metric.COMMITS: value, Metric.ISSUES: value}}
        aggregate_by: Method to aggregate metrics. Options: "sum", "average", "weighted"
    """
    if len(dev_metrics) == 0:
        raise ValueError("expected a non-empty dev_metrics")
    composite_scores = {}

    for dev_id, metrics in dev_metrics.items():
        if aggregate_by == "sum":
            score = sum(metrics.values())

        elif aggregate_by == "average":
            if len(metrics) > 0:
                score = sum(metrics.values()) / len(metrics)
            else:
                score = 0

        elif aggregate_by == "weighted":
            weights = {
                Metric.COMMITS: 0.5,
                Metric.ISSUES: 0.3,
                Metric.PULL_REQUESTS: 0.2
            }

            score = 0.0
            for metric, value in metrics.items():
                if metric in weights:
                    score += value * weights[metric]

        else:
            # default to `sum`
            score = sum(metrics.keys())  # does this look right?

        composite_scores[dev_id] = score

    return composite_scores


from collections import defaultdict
from enum import Enum


# for this assignment,
# the functions `count_contributions_by_metric`, `get_all_developers`, `get_all_repositories`, `fetch_commits`, `fetch_issues`, `fetch_prs`
# are dummy implementations that mock the real implementation of these functions. They return hardcoded values.
# When writing the test cases, pay attention to the values returned from these functions.
# You should construct test cases based on the return values of these functions.

def count_contributions_by_metric(developers, repos):
    """
    Counts the developers contributions across all repositories for specified metrics.

    Returns:
        dict: Dictionary with metric names as keys and counts as values.
            Example: {'commits': 15, 'issues': 3}
    """
    # this is merely a dummy implementation for ease of testing
    if len(repos) == 0:
        return {}
    contributions_by_developer = {}
    for dev in developers:
        contributions = defaultdict(int)
        contributions["commits"] = 15
        contributions["pull_requests"] = 4
        contributions["issues"] = 3

        contributions_by_developer[dev] = contributions

    return contributions_by_developer


def get_all_developers(org):
    # this is merely a dummy implementation for ease of testing
    if org == "ourorg":
        return ["Alice", "Bobby", "Charlie", "Doug", "Eliza"]
    elif org == "anotherorg":
        return ["Fabrice"]  #
    else:
        return []


def get_all_repositories(org):
    # this is merely a dummy implementation for ease of testing
    if org == "ourorg":
        return ["ourorg/repo1", "ourorg/repo2", "ourorg/repo3"]
    elif org == "anotherorg":
        return ["anotherorg/repo1"]
    else:
        return []


def fetch_commits(repo, developer):
    # this is merely a dummy implementation for ease of testing
    return 3


def fetch_issues(repo, developer):
    # this is merely a dummy implementation for ease of testing
    return 2


def fetch_prs(repo, developer):
    # this is merely a dummy implementation for ease of testing
    return 1


def count_contributions_by_repo(org, metrics, developer):
    """
    Counts the number of contributions made by a specific developer for each specified metric
    across all provided repositories.

    Args:
        org (str)
        metrics (list)
        developer (str)

    Returns:
        dict: A dictionary mapping repository identifiers to metric counts for the specified developer.
    """
    # initialization
    all_developers = get_all_developers(org)  # note that for the assignment,
    repos = get_all_repositories(org)  # we do not have to cover the statements and branches in the functions called

    # check that developer belongs to the org
    if developer not in all_developers:
        raise ValueError(f"the provided developer {developer} is not in the org {org}")

    contributions_count = {}

    for repo in repos:
        contributions_count[repo] = {}

        if Metric.COMMITS in metrics:
            commits = fetch_commits(repo, developer)
            contributions_count[repo]['commits'] = commits

        if Metric.ISSUES in metrics:
            issues = fetch_issues(repo, developer)
            contributions_count[repo] = {'issues': issues}  # weird: does this look like a bug?

    return contributions_count


def count_active_contributors(org, minimum_value_for_metrics):
    """
    Counts the number of contributors who has more activity in at least one metric in minimum_value_for_metrics

    Args:
        org: the organization name
        minimum_value_for_metrics: python dictionary mapping from a string key to an integer

    Returns:
        int: The count of active contributors who exceeds at least one of the minimum value in minimum_value_for_metrics

    """
    ### ??? TODO: As part of Question 3b, fix the bug in this function after writing a test case for Question 3a

    # validate input parameters
    if any(metric not in ["commits", "pull_requests", "issues"] for metric in minimum_value_for_metrics.keys()):
        raise ValueError("Expected a valid metric: commits, pull_requests, or issues")

    for metric, minimum_val in minimum_value_for_metrics.items():
        if minimum_val < 0 or minimum_val >= 10_000:
            raise ValueError("unlikely values for the metrics")

    all_developers = get_all_developers(org)
    repos = get_all_repositories(org)

    # initialization
    is_developer_active = False
    active_count = 0

    contributions = count_contributions_by_metric(all_developers, repos)

    for developer, dev_contributions in contributions.items():

        if dev_contributions['commits'] > minimum_value_for_metrics['commits']:
            is_developer_active = True
        if dev_contributions['pull_requests'] > minimum_value_for_metrics['pull_requests']:
            is_developer_active = True
        if dev_contributions['issues'] > minimum_value_for_metrics['issues']:
            is_developer_active = True
        else:
            is_developer_active = False

        if is_developer_active:
            active_count += 1

    return active_count


class TestScoreContributors(unittest.TestCase):
    def test_composite_score(self):
        # Question 1:
        # Inspect the following test case for compute_composite_score
        with self.assertRaises(ValueError):
            compute_composite_score({}, "sum")

        # Sample developer metrics
        dev_metrics1 = {
            "dev1": {Metric.COMMITS: 10, Metric.ISSUES: 5},
            "dev2": {Metric.COMMITS: 7, Metric.ISSUES: 12},
            "dev3": {Metric.COMMITS: 15, Metric.ISSUES: 3},
            "dev4": {}
        }

        expected = {
            "dev1": 15.0,
            "dev2": 19.0,
            "dev3": 18.0,
            "dev4": 0.0
        }
        result = compute_composite_score(dev_metrics1, "sum")
        self.assertEqual(result, expected)
        # Please write your answer to the following question as code comments prefixed with Answer:.
        # Question 1a: What is the statement coverage achieved by `test_composite_score` in testing `compute_composite_score`?
        #
        # Are these tests adequate (is there a bug that results in a TypeError missed by the test suite)?
        #   Which coverage criteria would be useful for writing a test case allowing a developer to observe the bug?
        #
        # Answer: The statement coverage achieved by the existing test cases is approximately 80%.
        # The test cases cover:
        # 1. The initial check for empty dev_metrics (raises ValueError)
        # 2. The "sum" aggregation method for developers with metrics
        # 3. The "sum" aggregation method for a developer with empty metrics
        #
        # However, the test cases do not cover:
        # 1. The "average" aggregation method
        # 2. The "weighted" aggregation method
        # 3. The default case (when aggregate_by is not "sum", "average", or "weighted")
        #
        # There is a bug in the default case where it tries to sum the keys of the metrics dictionary instead of the values:
        # score = sum(metrics.keys())  # This is incorrect, should be sum(metrics.values())
        #
        # Branch coverage would be useful for writing a test case that would allow a developer to observe this bug,
        # as it would ensure that all branches in the if-elif-else statement are executed.

        # Question 1b: Complete the test test suite to achieve 100% coverage
        # For this assignment, you do not have to fix the bug in `compute_composite_score`
        # When you write a test case that reveals the buggy behavior, ignore the exception
        # by using a try-except, or using self.assertRaises

        # Test case for "average" aggregation method
        dev_metrics2 = {
            "dev1": {Metric.COMMITS: 10, Metric.ISSUES: 5},
            "dev2": {Metric.COMMITS: 7, Metric.ISSUES: 12},
            "dev3": {Metric.COMMITS: 15, Metric.ISSUES: 3},
            "dev4": {}
        }

        expected_avg = {
            "dev1": 7.5,  # (10 + 5) / 2
            "dev2": 9.5,  # (7 + 12) / 2
            "dev3": 9.0,  # (15 + 3) / 2
            "dev4": 0.0  # empty metrics
        }
        result_avg = compute_composite_score(dev_metrics2, "average")
        self.assertEqual(result_avg, expected_avg)

        # Test case for "weighted" aggregation method
        dev_metrics3 = {
            "dev1": {Metric.COMMITS: 10, Metric.ISSUES: 5, Metric.PULL_REQUESTS: 2},
            "dev2": {Metric.COMMITS: 7, Metric.ISSUES: 12, Metric.PULL_REQUESTS: 3},
            "dev3": {Metric.COMMITS: 15, Metric.ISSUES: 3, Metric.PULL_REQUESTS: 1},
            "dev4": {}
        }
        
        expected_weighted = {
            "dev1": 6.9,  # 10*0.5 + 5*0.3 + 2*0.2
            "dev2": 7.7,  # 7*0.5 + 12*0.3 + 3*0.2
            "dev3": 8.6,  # 15*0.5 + 3*0.3 + 1*0.2
            "dev4": 0.0   # empty metrics
        }
        result_weighted = compute_composite_score(dev_metrics3, "weighted")
        
        # Use assertAlmostEqual for each developer's score to handle floating-point precision
        for dev_id in expected_weighted:
            self.assertAlmostEqual(result_weighted[dev_id], expected_weighted[dev_id], places=10)

        # Test case for default case (when aggregate_by is not "sum", "average", or "weighted")
        # This will reveal the bug where it tries to sum the keys instead of the values
        try:
            compute_composite_score(dev_metrics1, "invalid_method")
        except TypeError:
            # The bug causes a TypeError because it tries to sum the keys of the metrics dictionary
            pass

    def test_count_contributions_by_repos(self):
        # Question 2:
        # Look at the following test suite for count_contributions_by_repos
        count_contributions_by_repo("ourorg", [], "Alice")
        with self.assertRaises(ValueError):
            count_contributions_by_repo("emptyorg", [Metric.COMMITS, Metric.ISSUES], "Alice")
        with self.assertRaises(ValueError):
            count_contributions_by_repo("emptyorg", [Metric.COMMITS, Metric.ISSUES], None)

        actual = count_contributions_by_repo("ourorg", [Metric.COMMITS], "Alice")
        self.assertEqual(actual['ourorg/repo1']['commits'], 3)
        self.assertEqual(actual['ourorg/repo2']['commits'], 3)
        self.assertEqual(actual['ourorg/repo3']['commits'], 3)

        actual = count_contributions_by_repo("ourorg", [Metric.ISSUES], "Alice")
        self.assertEqual(actual['ourorg/repo1']['issues'], 2)
        self.assertEqual(actual['ourorg/repo2']['issues'], 2)
        self.assertEqual(actual['ourorg/repo3']['issues'], 2)

        # Please write your answer to the following question as code comments prefixed with Answer:.
        # Question 2a: What is the statement and branch coverage achieved by `test_count_contributions_by_repos` on `count_contributions_by_repos`?
        #   Note: ignore the coverage of the functions called by `count_contributions_by_repos`. We care only about the coverage of `count_contributions_by_repos`
        #
        #   Are these tests adequate (Is there a bug that results in incorrect return values)?
        #   Which additional coverage criteria would be useful for writing a test case allowing a developer to observe the bug?
        # Answer: The statement coverage achieved by the existing test cases is approximately 90%.
        # The test cases cover:
        # 1. The initial check for empty metrics list
        # 2. The check for developer not in the organization
        # 3. The case where Metric.COMMITS is in metrics
        # 4. The case where Metric.ISSUES is in metrics
        #
        # However, the test cases do not cover:
        # 1. The case where both Metric.COMMITS and Metric.ISSUES are in metrics
        #
        # There is a bug in the function where it overwrites the entire contributions_count[repo] dictionary when Metric.ISSUES is in metrics:
        # contributions_count[repo] = {'issues' : issues}  # This overwrites any previous values
        #
        # Path coverage would be useful for writing a test case that would allow a developer to observe this bug,
        # as it would ensure that all possible paths through the code are executed, including the path where both
        # Metric.COMMITS and Metric.ISSUES are in metrics.

        # Question 2b:
        # Your task is to complete the test suite
        # For this assignment, you do not have to fix the bug in `count_contributions_by_repos`
        # When you write a test case that reveals the buggy behavior, ignore the exception
        # by using a try-except, or using self.assertRaises

        # Test case for both Metric.COMMITS and Metric.ISSUES in metrics
        # This will reveal the bug where it overwrites the entire contributions_count[repo] dictionary
        actual = count_contributions_by_repo("ourorg", [Metric.COMMITS, Metric.ISSUES], "Alice")

        # The bug causes the 'commits' key to be missing from the dictionary
        # We can check this by trying to access the 'commits' key, which will raise a KeyError
        try:
            commits = actual['ourorg/repo1']['commits']
            # If we get here, the bug is not present
            self.fail("Expected KeyError, but no exception was raised")
        except KeyError:
            # The bug is present, as expected
            pass

    def test_bug1_in_count_active_contributors(self):
        # Question 3:
        # You have received the following bug report:
        #
        #                             Issue #1
        #                               Title:
        # count_active_contributors does not return the right number of active contributors
        #
        #                            Description:
        # The tool seems to be undercounting the number of active contributors.
        # In particular, it seems to be ignoring contributors who have a high number of commits
        # but do not post any issues on the issue tracker.
        #
        # ======================================================================================
        #
        # In this assignment, your task is write a test case that reveals the bug:
        # here are the existing test cases
        self.assertEqual(count_active_contributors("ourorg", {"commits": 1, "pull_requests": 1, "issues": 1}), 5)
        self.assertEqual(count_active_contributors("ourorg", {"commits": 50, "pull_requests": 50, "issues": 50}), 0)

        # Question 3a
        # Test case that reproduces the bug: a developer with high commits but no issues
        # The bug is in the logic where it sets is_developer_active to False in the else clause
        # after checking if issues > minimum_value_for_metrics['issues']
        # This causes the function to ignore developers who have high commits but no issues
        self.assertEqual(count_active_contributors("ourorg", {"commits": 10, "pull_requests": 1, "issues": 50}), 0)

        # Question 3b: fix the bug in count_active_contributors
        # The bug is in the logic where it sets is_developer_active to False in the else clause
        # after checking if issues > minimum_value_for_metrics['issues']
        # This causes the function to ignore developers who have high commits but no issues
        # The fix is to remove the else clause and only set is_developer_active to True when a condition is met
        # Here's the fixed version of the function:
        """
        def count_active_contributors(org, minimum_value_for_metrics):
            # validate input parameters
            if any(metric not in ["commits", "pull_requests", "issues"] for metric in minimum_value_for_metrics.keys()):
                raise ValueError("Expected a valid metric: commits, pull_requests, or issues")

            for metric, minimum_val in minimum_value_for_metrics.items():
                if minimum_val < 0 or minimum_val >= 10_000:
                    raise ValueError("unlikely values for the metrics")

            all_developers  = get_all_developers(org)
            repos           = get_all_repositories(org)

            # initialization
            active_count = 0

            contributions = count_contributions_by_metric(all_developers, repos)

            for developer, dev_contributions in contributions.items():
                is_developer_active = False
                
                if dev_contributions['commits'] > minimum_value_for_metrics['commits']:
                    is_developer_active = True
                if dev_contributions['pull_requests'] > minimum_value_for_metrics['pull_requests']:
                    is_developer_active = True
                if dev_contributions['issues'] > minimum_value_for_metrics['issues']:
                    is_developer_active = True

                if is_developer_active:
                    active_count += 1

            return active_count
        """

        # After the test cases, please write the answer to the following question as code comments prefixed with "Answer:"
        # Question 3c: What is one coverage criteria that would have guaranteed that the buggy behavior was observed during testing
        # Answer: Decision coverage would have guaranteed that the buggy behavior was observed during testing.
        # Decision coverage ensures that each decision in the code (each branch) is taken at least once.
        # In this case, the bug is in the else clause after checking if issues > minimum_value_for_metrics['issues'].
        # If we had tested the case where a developer has high commits but no issues, we would have observed the bug.
        # Decision coverage would have required us to test both the true and false branches of each condition,
        # which would have included the case where issues <= minimum_value_for_metrics['issues'].


if __name__ == '__main__':
    unittest.main()

# for this assignment, assertions are optional
