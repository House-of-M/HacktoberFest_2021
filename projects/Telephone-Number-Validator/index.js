function telephoneCheck(str) { //Checks if the input is a valid American phone number.
	let numRegex = /^(1\s?)?(\(\d{3}\)|\d{3})[\s\-]?\d{3}[\s\-]?\d{4}$/

	console.log("Phone number is: " + str);
	console.log(numRegex.test(str) + "\n");
	return numRegex.test(str);
}

telephoneCheck("1 555-555-5555"); //Returns true.
telephoneCheck("1 (555) 555-5555"); //Returns true.
telephoneCheck("5555555555"); //Returns true.
telephoneCheck("555-555-5555"); //Returns true.
telephoneCheck("(555)555-5555"); //Returns true.
telephoneCheck("1(555)555-5555"); //Returns true.
telephoneCheck("1 555 555 5555"); //Returns true.
telephoneCheck("1 456 789 4444"); //Returns true.

telephoneCheck("555-5555"); //Returns false.
telephoneCheck("5555555"); //Returns false.
telephoneCheck("1 555)555-5555"); //Returns false.
telephoneCheck("123**&!!asdf#"); //Returns false.
telephoneCheck("55555555"); //Returns false.
telephoneCheck("(6054756961)"); //Returns false.
telephoneCheck("2 (757) 622-7382"); //Returns false.
telephoneCheck("0 (757) 622-7382"); //Returns false.
telephoneCheck("-1 (757) 622-7382"); //Returns false.
telephoneCheck("2 757 622-7382"); //Returns false.
telephoneCheck("10 (757) 622-7382"); //Returns false.
telephoneCheck("27576227382"); //Returns false.
telephoneCheck("(275)76227382"); //Returns false.
telephoneCheck("2(757)6227382"); //Returns false.
telephoneCheck("2(757)622-7382"); //Returns false.
telephoneCheck("555)-555-5555"); //Returns false.
telephoneCheck("(555-555-5555"); //Returns false.
telephoneCheck("(555)5(55?)-5555"); //Returns false.

/* Regex Explanation:
^(1\s?)?(\(\d{3}\)|\d{3})[\s\-]?\d{3}[\s\-]?\d{4}$

^(1\s?)? 
	^       Matches pattern at beginning of the string.
	(...)   Means a Capture Group.
	1       Is looking for 1.
	\s?     ...Followed by an optional space.
	?       The ? outside the brackets means the Capture Group is optional.
                Altogether: Looks for the Country Code 1 at the very beginning. It is is optional.
	
(\(\d{3}\)|\d{3})
	(...)   Means a Capture Group.
	\(      Is looking for first bracket. (
	\d{3}   Is looking for exactly 3 digits.
	\)      Is looking for last bracket.
	|       An Or statement.
	\d{3}   Is looking for exactly 3 digits.
                Altogether: Looks for the 3-digit Area Code. Brackets are optional.
	
[\s\-]?		
	[...]   Match any character in this Set.
	\s      Looks for one space.
	\-      Looks for one dash.
	?       This ? means the Set is optional.
                Altogether: Looks for a dash or space after the Area Code. It is optional.
	
\d{3}
	\d{3}   Is looking for exactly 3 digits.
                Altogether: Looks for the first 3 digits of the number.
	
[\s\-]?		
	[...]   Match any character in this set.
	\s      Looks for one space.
	\-      Looks for one dash.
	?       This ? means the Set is optional.
                Altogether: Looks for a dash or space after the Area Code. It is optional.
	
\d{4}$
	\d{4}   Is looking for exactly 4 digits.
	$       Matches pattern at end of the string.
                Altogether: Looks for the last 4 digits of the number at the very end.
*/
