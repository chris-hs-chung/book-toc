# book-toc

Build a table of contents for pdf books.

Pdf books are hard to read because the table of contents usually don't match up with the pdf pages.
This python script takes care of that problem by generating a local webpage on your computer, that contains links to certain pages in the PDF book.

The only hard coding you have to do is to make json files for the books.

Jinja2 is used for the templating system. It's used in Flask. Speaking of which, I was going to use Flask instead of building my own framework, but I wanted this to be a local, serverless system. This makes sense because people's pdf books are not online; they are on their own computers.

## Tutorial
Install latest Python version and Jinja2

Create directories called "book_info" and "table_of_contents". I added these directories into the .gitignore file.

You will be hardcoding json files into the "book_info" directory.

The table of content webpages will show up in the "table_of_contents" directory.

### How to Hardcode book information
Create a json file inside "book_info" directory. The name of the file should be the name of the book.
You can name it however you want.

```
{
    "path" : "file:///D:/Books/harry_potter.pdf",
    "title" : "Harry Potter",
    "author" : "J.K. Rowling",
    "year" : 1999,
    "pageAdjust": 19,
    "front_cover" : "https://harrypotterpicture.com",
    "toc" : [
        ["Ch 1" , "Harry goes to Hogwarts" , 7] ,
        ["Ch 2" ,"Magic" , 25],
        ["Ch 3" , "Dumbledore" , 39]
    ]
}
```

The pageAdjust is very important. The problem with pdf books is that the real book's first page doesn't occur until chapter one starts. On pdf files, page one starts on, well, page one. So it has to be adjusted. You'll have to figure this out for yourself.

#### How to find pageAdjust
Inside the pdf book, go to the table of contents. Page one of the real book usually starts at chapter one. Go there inside the pdf, and note the pdf page number. Subract it by 1, then you got the pageAdjust number.

Test to see if the pageAdjust number is correct. Go back to the table of contents, pick any chapter. For example, chapter 3 of harry potter might be on page 30 of the real physical book. Add 30 with the pageAdjust number to get the pdf page number of chapter 3.

### Run the script
Run the script in the console. It will ask for the relative path of the book's json file.

For example: book_info\harey_potter_and_the_chamber_of_binary_numbers.json

If you are in a code editor like Visual studio, you can just right click on the file, and then click "Copy Relative Path"