# from measurement_converter_db import save_to_history

class MeasurementConverter:
    def __init__(self, string=None):
        self.string = string

    def get_letter_value(self, letter):
            """
            Get the numerical value of a letter.
            """
            if letter == 'z':
                return 26
            else:
                return ord(letter) - 96
            
    def pmc(self, string):
        """
        Parse the string and calculate the sum of letter values for each segment.
        """
        self.string = string
        result = []
        index = 0
        try:
            # Iterate through the string
            while index < len(string):
                if string[index].isalpha():
                    count = 0
                    # If the letter is z, add 26 to the count until you find the first non-z letter/char
                    if string[index] == 'z':
                        while string[index] == 'z':
                            count += self.get_letter_value(string[index])
                            index += 1
                        if string[index].isalpha():
                            count += self.get_letter_value(string[index])
                            index += 1
                    else:
                        count = self.get_letter_value(string[index])
                        index += 1
                        
                    sum_value = 0
                    i = index # i determains the start of the segment while index is a pointer to the current character
                    range = index + count

                    # Extract the sum of letter values for the segment
                    while i < (range):
                        if string[i].isalpha():
                            if string[i] == 'z':
                                range += 1
                                while string[i] == 'z':
                                    sum_value += self.get_letter_value(string[i])
                                    index += 1
                                    i += 1
                                if string[i].isalpha():
                                    sum_value += self.get_letter_value(string[i])
                            else:
                                sum_value += self.get_letter_value(string[i])
                        i += 1

                    result.append(sum_value)
                    index += count

                elif string[index] == '_':
                    # Append 0 and break the loop if the first character is '_' 
                    result.append(0)
                    break

                else:
                    # For any other character that is not a letter or '_', return "Invalid string input"
                    return "Invalid string input"
                    
        except:
            return "Invalid string input"
        return result

# Test cases
# mc = MeasurementConverter() 
# print(mc.pmc("dz_a_aazzaaa"))  # Output: [28, 53, 1]
# print(mc.pmc("za_a_a_a_a_a_a_a_a_a_a_a_a_azaaa"))  # Output: [40, 1]
# print(mc.pmc("aa"))  # Output: [1]
# print(mc.pmc("abbcc"))  # Output: [2, 6]
# print(mc.pmc("a_"))  # Output: [0]
# print(mc.pmc("abcdabcdab"))  # Output: [2, 7, 7]
# print(mc.pmc("abcdabcdab_"))  # Output: [2, 7, 7, 0]
# print(mc.pmc("zdaaaaaaaabaaaaaaaabaaaaaaaabbaa"))  # Output: [34]
# print(mc.pmc("za_a_a_a_a_a_a_a_a_a_a_a_a_azaaa"))  # Output: [40, 1]
# print(mc.pmc("zza_a_a_a_a_a_a_a_a_a_a_a_a_a_a_a_a_a_a_a_a_a_a_a_a_a_a_"))  # Output: [26]
# print(mc.pmc("__"))  # [0]
# print(mc.pmc("_zzzb"))  # [0]
# print(mc.pmc("_"))  # [0]
# print(mc.pmc("+"))  # Invalid output
