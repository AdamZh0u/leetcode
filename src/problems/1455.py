class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        words = sentence.split(' ')
        res = (index+1 for index,value in enumerate(words) if value.startswith(searchWord))
        return next(res, -1) 
    # list

# https://stackoverflow.com/questions/25653996/what-is-the-difference-between-list-and-iterator-in-python
# list is a mutable sequence of elements, while iterator is an object that can be used to traverse or iterate over a sequence of elements.
#  a list of a trillion integers would use more memory than most machines have available, which makes the iterator much more efficient
if __name__ == '__main__':
    sentence = "i love eating burger"
    searchWord = "burg"
    print(Solution().isPrefixOfWord(sentence, searchWord))