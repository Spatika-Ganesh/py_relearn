

import numbers


class Solution(object):
    # Q 1: 
    # Given an integer array nums sorted in non-decreasing order, remove the duplicates in-place 
    # such that each unique element appears only once. The relative order of the elements should be kept the same.
    #
    # Since it is impossible to change the length of the array in some languages,
    #  you must instead have the result be placed in the first part of the array nums.
    #  More formally, if there are k elements after removing the duplicates, 
    # then the first k elements of nums should hold the final result. 
    # It does not matter what you leave beyond the first k elements.
    #
    # Return k after placing the final result in the first k slots of nums.
    #
    # Do not allocate extra space for another array. 
    # You must do this by modifying the input array in-place with O(1) extra memory.
    # Date of attempt: Feb 16 2022
    def remove_duplicates_from_sorted_array(self, nums):
        k = 0 
        for i in range(len(nums)):
            if nums[k] != nums[i]: 
                k += 1
                nums[k] = nums[i]
        return k + 1

    # Q2: You are given an integer array prices where prices[i] is the price of a given stock on the ith day.
    # On each day, you may decide to buy and/or sell the stock. 
    # You can only hold at most one share of the stock at any time. 
    # However, you can buy it then immediately sell it on the same day.
    # Find and return the maximum profit you can achieve.
    def maxProfit(self, prices: List[int]) -> int:
        purchase_price = -1
        profit = 0
        for i in range(len(prices)-1):
            if prices[i+1] > prices[i]:
                if purchase_price == -1:
                    purchase_price = prices[i]
            else:
                if purchase_price != -1:    
                    profit += prices[i] - purchase_price
                    purchase_price = -1
            
        if purchase_price != -1:
            profit += prices[i+1] - purchase_price
                
        return profit
    

    #Q3 Given an array, rotate the array to the right by k steps, where k is non-negative.
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k = k % len(nums)
        nums[:] = nums[-k:] + nums[:-k]
    
    #Q4 Given an integer array nums, return true if any value appears at least twice in the array, 
    # and return false if every element is distinct.
    def containsDuplicate(self, nums: List[int]) -> bool:
        return len(set(nums)) != len(nums)

    #Q5 Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.
    # You must implement a solution with a linear runtime complexity and use only constant extra space.
    def singleNumber(self, nums: List[int]) -> int:
        xor = 0
        for i in nums:
            xor = xor ^ i
        return xor
    
    #Q6 Given two integer arrays nums1 and nums2, return an array of their intersection. 
    # Each element in the result must appear as many times as it shows in both arrays and you may return the result in any order.
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1_len = len(nums1)
        nums2_len = len(nums2)
        base_arr = nums1
        ref_arr = nums2
        if nums1_len > nums2_len:
            base_arr = nums2
            ref_arr = nums1
        index = 0
        while index < len(base_arr):
            if base_arr[index] in ref_arr:
                # remove from ref array
                ref_arr.remove(base_arr[index])
                index += 1
            else:
                #remove from base array
                base_arr.remove(base_arr[index])
        return base_arr

    #Q7 You are given a large integer represented as an integer array digits, where each digits[i] is the ith digit of the integer. 
    # The digits are ordered from most significant to least significant in left-to-right order. The large integer does not contain any leading 0's.
    # Increment the large integer by one and return the resulting array of digits.
    def plusOne(self, digits: List[int]) -> List[int]:
      
        if len(digits) == 0:
            return [1]
        elif digits[-1] ==9:
            digits = self.plusOne(digits[:-1])
            digits.append(0)
        else:
            digits[-1] += 1
        return digits
    
    