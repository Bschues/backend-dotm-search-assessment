# DOTM search

## Skills Required
 - [Google-fu](https://english.stackexchange.com/questions/19967/what-does-google-fu-mean)
 - File I/O
 - Operating System (os)
 - Argument parsing
 - Importing standard library modules
 
<hr>

This is a real-world problem that I recently helped a friend with.  He works at a law firm where they still use MSWord, and probably always will.  Along with FACSIMILE machines.  He wanted to try his hand at some python programming.

The **DOTM** file extension is a Microsoft Word File template developed by Microsoft Corporation in its version of 2007 and 2010 document template files. ... It is identical to .DOCX and .DOCM file in which the M stands for macro and the X stands for XML.

The law firm makes use of .dotm template files to bill for services.  These template files had hard-coded pricing amounts that needed to be updated manually.  But in their large collection of templates, they did not know which files contained pricing info.

By searching the dotm files for a '$' character, you can determine the subset of files that need to be reviewed and updated.  However, the dotm file is not a plain text file that can simply be read into python and examined ... Use your Google search and Stack Overflow skills to find out how dotm files can be decoded in python.  NOTE: Timebox your DOTM format research.  If you have not figured out the DOTM file format in 20 minutes, ask an instructor for a hint.

## Your Task
Write a python program named `dotm_search.py`.  
Your program should accept two cmdline arguments: First argument is the text to search. 
The second argument is an OPTIONAL directory of .dotm files to scan.  If this argument is omitted,
the default path to search is the current directory.
```
python dotm_search.py --dir ./dotm_files "$" 
python dotm_search.py "other text"
```

- Your program should print the full path name of each file that was found to contain the search text.  If the file contains multiple matches, just count it as a single match.
- For context, print a partial line of the dotm text that was found to contain the search text.  Limit the printed line to +/- 40 characters on each side of the matched text.  Example: `"...alculated on a per article basis (up to $500 each), the total false marking penal..."`
- Count the total number of file matches as well as total number of files searched, and display the results before exiting.


## Some Tips
- Disregard (do not search) files without a .dotm extension.  Don't count them as searched files either.
- Inside the `.dotm` file, the section to search is `'word/document.xml'`
- You may wish to investigate the [argparse](https://docs.python.org/2/howto/argparse.html) standard library.
- Use the python idiom `if __name__ == '__main__'` in your program.

## Sample Output
```
/Users/piero/Documents/github/kenzie/backend-dotm-search-assessment/dotm_search.py --dir ./dotm_files $
Searching directory ./dotm_files for text '$' ...
Match found in file ./dotm_files/P416NO.dotm
   ...tion fee for this case is approximately $ </w:t></w:r><w:r><w:rPr><w:highlight w...
Match found in file ./dotm_files/TM097IP.dotm
   ...:highlight w:val="yellow"/></w:rPr><w:t>$</w:t></w:r><w:r w:rsidR="00000C16"><w:...
Match found in file ./dotm_files/P620US.dotm
   ...><w:tab/><w:t>Credit Card Form PTO-2038 $</w:t></w:r><w:r w:rsidRPr="00D53D14"><...
Match found in file ./dotm_files/OT002US.dotm
   ...0D17087"><w:tab/><w:t>The filing fee of $</w:t></w:r><w:r w:rsidRPr="00D17087"><...
Match found in file ./dotm_files/TM250US.dotm
   ...an: (a) monitor their application (cost $</w:t></w:r><w:r w:rsidRPr="006716FE"><...
Match found in file ./dotm_files/G003.dotm
   ...rent hourly rate on this matter will be $</w:t></w:r><w:r w:rsidRPr="00CE01BA"><...
Match found in file ./dotm_files/D077US.dotm
   ... so at your request for a cost of about $10.00 per page. Errors can be addressed...
Match found in file ./dotm_files/TM406JP.dotm
   ...:highlight w:val="yellow"/></w:rPr><w:t>$</w:t></w:r><w:r w:rsidR="00D41DC7"><w:...
Match found in file ./dotm_files/P045US.dotm
   ... C.F.R. §1.78(a)(3)), in the amount of $</w:t></w:r><w:r w:rsidRPr="000A00EE"><...
Match found in file ./dotm_files/TM079US.dotm
   ...:highlight w:val="yellow"/></w:rPr><w:t>$</w:t></w:r><w:r w:rsidR="006B14A9"><w:...
Match found in file ./dotm_files/P454EP.dotm
   .../><w:snapToGrid w:val="0"/></w:rPr><w:t>$ Estimate</w:t></w:r></w:p></w:tc></w:t...
Match found in file ./dotm_files/P618US.dotm
   ...rovided along with the requisite fee of $</w:t></w:r><w:r w:rsidRPr="00294C96"><...
Match found in file ./dotm_files/TM095.dotm
   ...:highlight w:val="yellow"/></w:rPr><w:t>$</w:t></w:r><w:r w:rsidR="002A0F56"><w:...
Match found in file ./dotm_files/P408IE.dotm
   ...f the patent grant fee is approximately $</w:t></w:r><w:r><w:rPr><w:highlight w:...
Match found in file ./dotm_files/C004US.dotm
   ...="25"/><w:szCs w:val="28"/></w:rPr><w:t>$</w:t></w:r><w:r w:rsidRPr="00E441AC"><...
Match found in file ./dotm_files/TM203US.dotm
   ...:highlight w:val="yellow"/></w:rPr><w:t>$</w:t></w:r><w:r w:rsidR="007C35CC"><w:...
Match found in file ./dotm_files/P415KR.dotm
   ... xml:space="preserve"> to pay the fees ($</w:t></w:r><w:r><w:rPr><w:highlight w:...
Match found in file ./dotm_files/TM903US.dotm
   ...n of the sum of One and No/100 Dollars ($1.00) and other good and valuable consi...
Match found in file ./dotm_files/PS001USR.dotm
   ...results to you with a maximum budget of $</w:t></w:r><w:r w:rsidRPr="005330AB"><...
Match found in file ./dotm_files/TM410AU.dotm
   ...:highlight w:val="yellow"/></w:rPr><w:t>$</w:t></w:r><w:r w:rsidR="00C536F3"><w:...
Match found in file ./dotm_files/P030US.dotm
   ... page of the patent for a cost of about $100.00.</w:t></w:r><w:r w:rsidRPr="0050...
Match found in file ./dotm_files/P041US.dotm
   ...nt on your behalf for a total charge of $</w:t></w:r><w:r w:rsidRPr="00F931BE"><...
Match found in file ./dotm_files/P411CN.dotm
   ...><w:r><w:t>, at a cost of approximately $</w:t></w:r><w:r><w:rPr><w:highlight w:...
Match found in file ./dotm_files/TM408IP.dotm
   ..."preserve"> Swiss Francs (approximately $</w:t></w:r><w:r w:rsidRPr="00CF5637"><...
Match found in file ./dotm_files/PS001US.dotm
   ...patentability search at a cost of about $</w:t></w:r><w:r w:rsidRPr="00A744A7"><...
Match found in file ./dotm_files/TM049US.dotm
   ...:highlight w:val="yellow"/></w:rPr><w:t>$</w:t></w:r><w:r w:rsidR="007917B1"><w:...
Match found in file ./dotm_files/TM102US.dotm
   ...uch monitoring for a price of typically $400 or more. </w:t></w:r><w:r w:rsidRPr...
Match found in file ./dotm_files/P043US.dotm
   ...nt on your behalf for a total charge of $</w:t></w:r><w:r w:rsidRPr="00FC5A85"><...
Match found in file ./dotm_files/L003.dotm
   ...></w:rPr><w:t>My current hourly rate is $</w:t></w:r><w:r w:rsidRPr="005F11CD"><...
Match found in file ./dotm_files/TM049UST.dotm
   ...:highlight w:val="yellow"/></w:rPr><w:t>$</w:t></w:r><w:r w:rsidR="00A16186"><w:...
Match found in file ./dotm_files/G004.dotm
   ... costs are estimated to be greater than $5,000.</w:t></w:r><w:r w:rsidR="000413C...
Match found in file ./dotm_files/PS009USR.dotm
   ...<w:highlight w:val="cyan"/></w:rPr><w:t>$10,000</w:t></w:r><w:r><w:t xml:space="...
Match found in file ./dotm_files/TM300UST.dotm
   ...ling such a declaration is estimated at $600.  </w:t></w:r></w:p><w:p w:rsidR="0...
Match found in file ./dotm_files/P520PC.dotm
   ...xml:space="preserve"> for approximately $</w:t></w:r><w:r w:rsidRPr="001061A0"><...
Match found in file ./dotm_files/TM035IP.dotm
   .... The cost is fairly nominal (currently $175 per year per mark). If you wish us ...
Match found in file ./dotm_files/P408MX.dotm
   ...:highlight w:val="yellow"/></w:rPr><w:t>$1,250</w:t></w:r><w:r w:rsidRPr="009D6F...
Match found in file ./dotm_files/P015UST.dotm
   ...consideration of the sum of One Dollar ($1.00) and other good, valuable and suff...
Match found in file ./dotm_files/TM097US.dotm
   ...:highlight w:val="yellow"/></w:rPr><w:t>$</w:t></w:r><w:r w:rsidR="007744F0"><w:...
Match found in file ./dotm_files/TM097UST.dotm
   ...:highlight w:val="yellow"/></w:rPr><w:t>$</w:t></w:r><w:r w:rsidR="00877C43"><w:...
Match found in file ./dotm_files/TM052US.dotm
   ...:highlight w:val="yellow"/></w:rPr><w:t>$</w:t></w:r><w:r w:rsidR="00F86768"><w:...
Match found in file ./dotm_files/TM603US.dotm
   ...><w:tab/><w:t>Credit Card Form PTO-2038 $</w:t></w:r><w:r w:rsidRPr="001F172C"><...
Match found in file ./dotm_files/PS004US.dotm
   ...ase limit your total search expenses to $</w:t></w:r><w:r w:rsidRPr="00AF22A3"><...
Match found in file ./dotm_files/P089USR.dotm
   ... so at your request for a cost of about $5.00 per column. Based upon this review...
Match found in file ./dotm_files/TM904US.dotm
   ...n of the sum of One and No/100 Dollars ($1.00) and other good and valuable consi...
Match found in file ./dotm_files/P037US.dotm
   ...2F3B"><w:t>money order in the amount of $_______.</w:t></w:r></w:p><w:p w:rsidR=...
Match found in file ./dotm_files/P043USG.dotm
   ...nt on your behalf for a total charge of $</w:t></w:r><w:r w:rsidRPr="00C32979"><...
Match found in file ./dotm_files/P039US.dotm
   ...nt on your behalf for a total charge of $</w:t></w:r><w:r w:rsidRPr="000B2863"><...
Match found in file ./dotm_files/P039US.dotm
   ...:highlight w:val="yellow"/></w:rPr><w:t>$</w:t></w:r><w:r w:rsidRPr="000B2863"><...
Match found in file ./dotm_files/PS004USR.dotm
   ...<w:t>know if you feel that a search for $</w:t></w:r><w:r w:rsidR="00130026" w:r...
Match found in file ./dotm_files/TM009US.dotm
   ...:highlight w:val="yellow"/></w:rPr><w:t>$</w:t></w:r><w:r w:rsidR="0005463F"><w:...
Match found in file ./dotm_files/P408PT.dotm
   ...he total of these fees is approximately $ </w:t></w:r><w:r><w:rPr><w:highlight w...
Match found in file ./dotm_files/TM099US.dotm
   ...:highlight w:val="yellow"/></w:rPr><w:t>$</w:t></w:r><w:r w:rsidR="00474522"><w:...
Match found in file ./dotm_files/P200US.dotm
   ...w:rPr><w:t>money order in the amount of $_______.</w:t></w:r></w:p><w:p w:rsidR=...
Match found in file ./dotm_files/P030UST.dotm
   ... page of the patent for a cost of about $100.00. </w:t></w:r></w:p><w:p w:rsidR=...
Match found in file ./dotm_files/P603US.dotm
   ...><w:tab/><w:t>Credit Card Form PTO-2038 $</w:t></w:r><w:r w:rsidRPr="00BC627D"><...
Match found in file ./dotm_files/TM101US.dotm
   ...:highlight w:val="yellow"/></w:rPr><w:t>$</w:t></w:r><w:r w:rsidR="00E902D4"><w:...
Match found in file ./dotm_files/TM062US.dotm
   ...0A70E6F"><w:tab/><w:t>The filing fee of $</w:t></w:r><w:r w:rsidRPr="00A70E6F"><...
Match found in file ./dotm_files/TM025US.dotm
   ...:highlight w:val="yellow"/></w:rPr><w:t>$</w:t></w:r><w:r w:rsidR="0097015F"><w:...
Match found in file ./dotm_files/P089US.dotm
   ... so at your request for a cost of about $5.00 per column.  Errors can be address...
Match found in file ./dotm_files/P521PC.dotm
   ...uthorizing by credit card the amount of $</w:t></w:r><w:r w:rsidRPr="00D12AB6"><...
Match found in file ./dotm_files/P533PC.dotm
   ...ng this application to be approximately $</w:t></w:r><w:r w:rsidRPr="00D6625E"><...
Match found in file ./dotm_files/P412IL.dotm
   ...ing all official fees, is approximately $</w:t></w:r><w:r><w:rPr><w:highlight w:...
Match found in file ./dotm_files/TM049IP.dotm
   ...:highlight w:val="yellow"/></w:rPr><w:t>$400 plus $325 per Class?</w:t></w:r><w:...
Match found in file ./dotm_files/UM082US.dotm
   ...preserve"> money order in the amount of $</w:t></w:r><w:sdt><w:sdtPr><w:id w:val...
Match found in file ./dotm_files/TM411JP.dotm
   ...:highlight w:val="yellow"/></w:rPr><w:t>$</w:t></w:r><w:r w:rsidR="00375FCB"><w:...
Match found in file ./dotm_files/TM103US.dotm
   ...:highlight w:val="yellow"/></w:rPr><w:t>$</w:t></w:r><w:r w:rsidR="00563616"><w:...
Match found in file ./dotm_files/P453EP.dotm
   ...d cost of the printing and grant fee is $</w:t></w:r><w:r w:rsidRPr="002623D2"><...
Match found in file ./dotm_files/P418EP.dotm
   ...isional application to be approximately $</w:t></w:r><w:r w:rsidRPr="002B62D2"><...
Match found in file ./dotm_files/P412RU.dotm
   ...:highlight w:val="yellow"/></w:rPr><w:t>$500.00</w:t></w:r><w:r><w:t xml:space="...
Match found in file ./dotm_files/TM035US.dotm
   ...:highlight w:val="yellow"/></w:rPr><w:t>$</w:t></w:r><w:r w:rsidR="00786608"><w:...
Match found in file ./dotm_files/P646US.dotm
   ...r><w:color w:val="000000"/></w:rPr><w:t>$</w:t></w:r><w:r w:rsidRPr="00F17D10"><...
Match found in file ./dotm_files/TM409IP.dotm
   ...:highlight w:val="yellow"/></w:rPr><w:t>$</w:t></w:r><w:r w:rsidR="00F95017"><w:...
Total dotm files searched: 799
Total dotm files matched: 72
```


Here's a sneak peek inside a dotm file:

```
PK!��Ǉ�4\[Content\_Types\].xml �(��U�n�0��?������C��u�^)re� �N��\]=��m,�q| �;3;K�ί�L�� D�l�.�K�J��\]����.�Ȓ��\*Q99�Cd׋��櫽��P��9� �O�G�#b�<X�)\]0�7���X���>p�,��k���B)�&�'Zn�ڲ�=WS�Lx\_i)���U���+K-!��!� ���Tq�O�i'7�Ȇ1n�����z��.�3����A����.(���2$�鲮C2�IdF��V���Emj���m���vC�rљ��$RY|�����ma{\[z�j�kq4;�5��'��~��$�Hp��z�!#��F�W�^A�;����Ͳ,�yLQBϪ�`-ų�q6@$������c�<\*��/gS�|TH�Z��}=*�:��򨄒:���Mo�z�QHS x�=�50C�Ե��GS.�"��䩣Sj;�\]�H#�d����  
�ܼ���_��PK!���N_rels/.rels �(����JA���a�}7�  
"���H�w"����w̤ھ�� �P�^����O֛���;�<�aYՠ؛`G�kxm��PY�\[��g  
Gΰino�/<���<�1��ⳆA$>"f3��\\�ȾT��I S����������W����Y  
ig�@��X6_�\]7~  
f��ˉ�ao�.b*lI�r�j)�,l0�%��b�  
```
