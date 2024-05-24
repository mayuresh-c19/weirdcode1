import webapp2 

htmlForm = """

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Calculator</title>
</head>
<body>
    <h1>Calculator</h1>
    <form action="/" method="post">
        <label for="num1">Number 1 : </label>
        <input type="number" id="num1" name="num1" required><br><br>

        <label for="num2">Number 2 : </label>
        <input type="number" id="num2" name="num2" required><br><br>

        <label for="operation">Operation : </label>
        <select name="operation" id="operation">
            <option value="add">+</option>
            <option value="sub">-</option>
            <option value="div">/</option>
            <option value="mul">*</option>
        </select><br><br>

        <input type="submit" value="Calculate">
        
    </form>
</body>
</html>

"""

class MainPage(webapp2.RequestHandler):
    def get(self):
        self.response.write(htmlForm)
    
    def post(self):
        try:
            num1 = float(self.request.get('num1'))
            num2 = float(self.request.get('num2'))
            operation = self.request.get('operation')

            if operation == 'add':
                result = num1 + num2
            elif operation == 'sub':
                result = num1 - num2
            elif operation == 'mul':
                result = num1 * num2
            elif operation == 'div':
                if num2 == 0:
                    result = "Error Not Divisible by 0"
                else:
                    result = num1/num2
            else:
                result = "Invalid operation"
            
            self.response.write(htmlForm)
            self.response.write("<h2>Result: {}</h2>".format(result))
        except ValueError:
            self.response.write(htmlForm)
            self.response.write("<h2>Error! Invalid Input</h2>")


app = webapp2.WSGIApplication([('/',MainPage)], debug = True)