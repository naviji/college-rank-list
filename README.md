### How to run
```

pip install -r requirements.txt
python main.py

```

Input:
A URL for the exam result from KTU website that you need to convert to a CSV file.  
eg: [S7 exam results 2018](https://ktu.edu.in/eu/res/viewExamResults.htm?type=Y8ZBNv%2BX3g0jDc1D71uSPGnLoYDc1PU9ntOC%2FO3gYdE%3D&examDefIdEnr=pJoFjPvjDnPZ3l8bD0YsASOeWjjdhrLmJlCm1IqZIHA%3D&publishId=FblF%2Bs1NwslZO00wrxm7kkSYfMqAi%2Fezke2lOpsNTY0%3D)


Output:
1. Downloaded PDF files in the pdf folder.
2. TXT files after PDF to TXT conversion in the text folder.
3. A CSV file in the csv folder with the exam name.  
eg: B.Tech S7 Exam Dec 2018 (S7 Result).csv

#### CSV column names
Column 1 : Register number  
Column 2 : Department  
Column 3 : Couse code  
Column 4 : Grade in the course  
Column 5 : College name  
