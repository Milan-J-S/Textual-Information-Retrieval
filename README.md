This project extracts the specsheet of a smartphone from reviews scraped from the web. The specs are extracted using basic NLP techniques. The methodology used can be extended to other information retrieval applications

-----------------------------------------------------------------------------------------------------------------------------------

The corpus is generated from scraping the web for reviews of mobile phones from the 'Android Central' website.
Each text file contains the text review. The contents are cleaned to remove all html tags occuring within the text content

The template is the specifications of the mobile phone. This includes:
1. Manufacturer
2. Model
3. Camera Resolution
4. Lens Aperture
5. Front Camera Resolution
6. Video Recording
7. Screen resolution
8. Screen Size
9. Battery Capacity
10. OS
11. RAM
12. Storage
13. Processor
14. Price

The template is populated using word tokenization, POS tagging and chunking. Regexes are used to extract data.

Required Libraries:
1. NLTK
2. re   (Python regex library)
3. os


How to run:
1. The text files are in a folder named 'corpus'
2. The program file is 'infoext.py'
3. Run the program using the command 'python infoext.py'
4. The template is populated and printed for all the documents in the corpus
5. A new file can be added and it's information can be extracted 
