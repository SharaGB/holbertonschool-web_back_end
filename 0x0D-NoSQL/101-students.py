#!/usr/bin/env python3
"""
Top students
"""
import pymongo


def top_students(mongo_collection):
    """
    find and sort
    """
    return mongo_collection.aggregate([
        {"$project": {"name": "$name", "averageScore": {"$avg": "$topics.score"}}},
        {"$sort": {"averageScore": -1}}
    ])
