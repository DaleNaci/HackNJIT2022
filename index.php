
<html lang="en">
<head>
    <meta charset="UTF-8" />
    <title>NJIT Schedule Generator</title>
    <link rel="stylesheet" href="main.css">
    <!-- CSS only -->
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.2.2/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-Zenh87qX5JnK2Jl0vWa8Ck2rdkQ2Bzep5IDxbcnCeuOxjzrPF/et3URy9Bv1WTRi" crossorigin="anonymous">
    
</head>
<body>
    <header>
        <h1>NJIT Schedule Generator</h1>
    </header>
    <main>
        <script src="https://cdnjs.cloudflare.com/ajax/libs/jquery/3.3.1/jquery.min.js"></script>
        <form action="generate.php" method="post">
            <div class="container1">
                <button class="btn btn-outline-secondary">Add Course &nbsp; 
                    <span>+ </span>
                </button>
                <p><br>Course Category &nbsp &nbsp &nbsp &nbsp &nbsp &nbsp &nbsp &nbsp &nbsp &nbsp &nbsp Course Number</p>
                <div id="custom-margin"><input type="course-category" name="course1"><input type="course-number" name="num1"></div>
            </div>
            <input id="x" type="hidden" name="x" value="0" />
            <button type="submit" class="btn btn-outline-success">Generate</button>
        </form>
        
        <script>
            $(document).ready(function() {
            var max_fields = 6;
            var wrapper = $(".container1");
            var add_button = $(".btn.btn-outline-secondary");
    
            var x = 1;
            $(add_button).click(function(e) {
                e.preventDefault();
                if (x < max_fields) {
                    x++;
                    document.getElementById("x").value = x;
                    $(wrapper).append('<div><input type="course-category" name="course' + x + '"/><input type="course-number" name="num' + x + '"/><button class="btn btn-outline-secondary btn-sm">Delete</button></div>');
                } else {
                alert('You Reached the limits')
                }
            });
    
            $(wrapper).on("click", ".btn.btn-outline-secondary.btn-sm", function(e) {
                e.preventDefault();
                $(this).parent('div').remove();
                x--;
                document.getElementById("x").value = x;
            })

        });
        </script>
    </main>
    <!--
    <main>
        <form>
            <div class="form-group" >
                <label for="number-of-classes">Number of Classes</label>
                <select class="form-control text-center" id="number-of-classes">
                  <option>1</option>
                  <option>2</option>
                  <option>3</option>
                  <option>4</option>
                  <option>5</option>
                  <option>6</option>
                </select>
              </div>
            <div class="form-group">
                <label for="class-category">Class Category:</label>
                <input type="class-category" class="form-control" id="class-category">
            </div>
            <div class="form-group">
                <label for="class-number">Class Number:</label>
                <input type="class-number" class="form-control" id="class-number">

                <button class="add_form_field">Add New Field &nbsp; 
                  <span style="font-size:16px; font-weight:bold;">+ </span>
                </button>
            </div>

            <button type="submit" class="btn btn-outline-success">Generate</button>
        </form>
    
    </main>

    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.2.2/dist/js/bootstrap.bundle.min.js" integrity="sha384-OERcA2EqjJCMA+/3y+gxIOqMEjwtxJY7qPCqsdltbNJuaOe923+mo//f6V8Qbsw3" crossorigin="anonymous"></script>
    <script>    
        $(document).ready(function() {
            var max_fields = 6;
            var wrapper = $("form-group");
            var add_button = $(".add_form_field");

            var x = 1;
            $(add_button).click(function(e) {
                e.preventDefault();
                if (x < max_fields) {
                    x++;
                    $(wrapper).append('<div class="form-group"><label for="class-category">Class Category:</label><input type="class-category" class="form-control" id="class-category"></div>');
                    $(wrapper).append('<div class="form-group"><label for="class-number">Class Number:</label><input type="class-number" class="form-control" id="class-number"></div>');
             //add input box
                } else {
                    alert('You Reached the limits')
                }
            });

            $(wrapper).on("click", ".delete", function(e) {
                e.preventDefault();
                $(this).parent('div').remove();
                x--;
            })
        });
    </script>
    -->

</body>
</html>