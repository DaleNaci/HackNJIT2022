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
            <!--Course List-->
            <div class="section">
                <h4>Course List:</h4>
                <p>Add a maximum of 6 courses to the list.</p>
            </div>
            <div class="container1">
                <p id="courses">Course Category &nbsp &nbsp &nbsp &nbsp &nbsp &nbsp &nbsp &nbsp Course Number</p>
                <div id="custom-margin"><input type="course-category" name="course1"><input type="course-number" name="num1"></div>
            </div>
            <input id="x" type="hidden" name="x" value="0" />
            <div class="coursebutton">
                <button class="btn btn-outline-secondary">Add Course &nbsp; 
                    <span>+ </span>
                </button>
            </div>
            <br>

            <!-- Schedule Preferences-->
            <div class="section">
                <h4>Schedule Preferences:</h4>
                <p>Select your priority from 1-5 for each preference.<br>(0 = no preference, 1 = low priority, 5 = high priority)</p>
            </div>
            <div class="preferences">
                <select id="priority1" name="priority1">
                    <option value="0">0</option>
                    <option value="1">1</option>
                    <option value="2">2</option>
                    <option value="3">3</option>
                    <option value="4">4</option>
                    <option value="5">5</option>
                </select>
                <label for="priority1"><b>No 6:00pm-9:00pm Class</b></label>
                <br>

                <select id="priority2" name="priority2">
                    <option value="0">0</option>
                    <option value="1">1</option>
                    <option value="2">2</option>
                    <option value="3">3</option>
                    <option value="4">4</option>
                    <option value="5">5</option>
                </select>
                <label for="priority2"><b>No 8:30am Class</b></label>
                <br>

                <select id="priority3" name="priority3">
                    <option value="0">0</option>
                    <option value="1">1</option>
                    <option value="2">2</option>
                    <option value="3">3</option>
                    <option value="4">4</option>
                    <option value="5">5</option>
                </select>
                <label for="priority3"><b>No Monday Class</b></label>
                <br>

                <select id="priority4" name="priority4">
                    <option value="0">0</option>
                    <option value="1">1</option>
                    <option value="2">2</option>
                    <option value="3">3</option>
                    <option value="4">4</option>
                    <option value="5">5</option>
                </select>
                <label for="priority4"><b>No Friday Class</b></label>
                <br>

                <select id="priority5" name="priority5">
                    <option value="0">0</option>
                    <option value="1">1</option>
                    <option value="2">2</option>
                    <option value="3">3</option>
                    <option value="4">4</option>
                    <option value="5">5</option>
                </select>
                <label for="priority5"><b>Rate My Professor</b></label>
                <br>
                <br>
            </div>
            <div class="section">
                <button type="submit" class="btn btn-outline-success">Generate</button>
            </div>
        </form>
        
        <script>
            $(document).ready(function() {

            /*add courses*/
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
                }
            });
    
            $(wrapper).on("click", ".btn.btn-outline-secondary.btn-sm", function(e) {
                e.preventDefault();
                $(this).parent('div').remove();
                x--;
                document.getElementById("x").value = x;
            });
        });
        </script>
    </main>
</body>
</html>
