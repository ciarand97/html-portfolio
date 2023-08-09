document.addEventListener("DOMContentLoaded", function() {
    const generateButton = document.getElementById("generateButton");
    const departmentInput = document.getElementById("department");
    const monthInput = document.getElementById("month");
    const yearInput = document.getElementById("year");
    const outputElement = document.getElementById("output");

    const monthMap = {
        "January": "01",
        "February": "02",
        "March": "03",
        "April": "04",
        "May": "05",
        "June": "06",
        "July": "07",
        "August": "08",
        "September": "09",
        "October": "10",
        "November": "11",
        "December": "12"
    };

    generateButton.addEventListener("click", function() {
        const department = departmentInput.value;
        const month = monthInput.value;
        const year = yearInput.value;

        if (department && month && year && monthMap.hasOwnProperty(month)) {
            const processedDepartment = processDepartment(department);
            const generatedOutput = generateOutput(processedDepartment, monthMap[month], year);
            outputElement.textContent = generatedOutput;
        }
    });

    function processDepartment(department) {
        return "L10N_" + department.replace(/[aeiouAEIOU]/g, "").toUpperCase();
    }

    function generateOutput(processedDepartment, month, year) {
        const formattedYear = year.slice(-2);
        const randomNumber = Math.floor(Math.random() * 10000).toString().padStart(4, "0");
        return `${processedDepartment}${month}${formattedYear}${randomNumber}`;
    }
});
