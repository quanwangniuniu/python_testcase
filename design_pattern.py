from typing import Dict, List, Tuple
from abc import ABC, abstractmethod
from enum import Enum


### Part 3 of the assignment ###
# Question 1: What is the design pattern implemented by the RankContributors and ScoringMethod class?
# Answer: The design pattern implemented by the RankContributors and ScoringMethod class is the Strategy Pattern.
# 
# The Strategy Pattern defines a family of algorithms, encapsulates each one, and makes them interchangeable.
# It lets the algorithm vary independently from clients that use it.
# 
# In this implementation:
# 1. ScoringMethod is an abstract base class that defines the interface for all concrete scoring algorithms.
# 2. SumScoringMethod, AverageScoringMethod, and WeightedScoringMethod are concrete implementations of the scoring algorithm.
# 3. RankContributors is the client that uses the scoring algorithm. It has a reference to a ScoringMethod object
#    and delegates the computation of the score to that object.
# 
# This design allows for:
# 1. Encapsulation of different scoring algorithms in separate classes.
# 2. Runtime selection of the scoring algorithm by passing different ScoringMethod objects to the RankContributors constructor.
# 3. Easy addition of new scoring algorithms by creating new classes that implement the ScoringMethod interface.
#
# The Strategy Pattern is appropriately used in this case. The pros include:
# 1. Flexibility: Different scoring algorithms can be easily swapped at runtime.
# 2. Extensibility: New scoring algorithms can be added without modifying existing code (Open/Closed Principle).
# 3. Encapsulation: Each scoring algorithm is encapsulated in its own class, making the code more maintainable.
# 
# The cons include:
# 1. Increased number of classes: Each algorithm requires a separate class, which can lead to a large number of small classes.
# 2. Potential over-engineering: If there are only a few algorithms that are unlikely to change, the pattern might be unnecessary.
# 
# In this specific implementation, the Strategy Pattern is justified because:
# 1. There are multiple scoring algorithms (sum, average, weighted) with different behaviors.
# 2. The scoring algorithm might need to be changed at runtime based on user preferences or requirements.
# 3. New scoring algorithms might be added in the future as the system evolves.

class Metric(Enum):
    COMMITS = "commits"
    PULL_REQUESTS = "pull_requests"
    ISSUES = "issues"
    # note that in design_pattern.py, we removed the `composite` enum. This is deliberate.


class ScoringMethod(ABC):
    @abstractmethod
    def compute_score(self, metrics: Dict[Metric, float]) -> float:
        pass


class SumScoringMethod(ScoringMethod):
    def compute_score(self, metrics: Dict[Metric, float]) -> float:
        return sum(metrics.values())


class AverageScoringMethod(ScoringMethod):
    def compute_score(self, metrics: Dict[Metric, float]) -> float:
        if len(metrics) == 0:
            return 0.0
        return sum(metrics.values()) / len(metrics)


class WeightedScoringMethod(ScoringMethod):
    def __init__(self):
        self.weights = {
            Metric.COMMITS: 0.5,
            Metric.ISSUES: 0.3,
            Metric.PULL_REQUESTS: 0.2
        }

    def compute_score(self, metrics: Dict[Metric, float]) -> float:
        return sum(
            value * self.weights.get(metric, 0.0)
            for metric, value in metrics.items()
        )


class RankContributors:
    def __init__(self, scoring_method: ScoringMethod):
        self.scoring_method = scoring_method

    def rank(self, dev_metrics: Dict[str, Dict[Metric, float]]) -> List[Tuple[str, float]]:
        if not dev_metrics:
            raise ValueError("expected a non-empty dev_metrics")

        scored = [
            (dev_id, self.scoring_method.compute_score(metrics))
            for dev_id, metrics in dev_metrics.items()
        ]

        return sorted(scored, key=lambda x: x[1], reverse=True)


dev_metrics = {
    "dev1": {Metric.COMMITS: 10, Metric.ISSUES: 5},
    "dev2": {Metric.COMMITS: 7, Metric.ISSUES: 12},
    "dev3": {Metric.COMMITS: 15, Metric.ISSUES: 3},
    "dev4": {}
}

ranker = RankContributors(SumScoringMethod())
print("Sum:", ranker.rank(dev_metrics))

##### Answer the question at the top of this file #####
