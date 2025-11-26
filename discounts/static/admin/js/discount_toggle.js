(function() {
    function toggleFields() {
        const type = document.getElementById("id_discount_type").value;

        const euro = document.querySelector("div.field-discount_euro");
        const euroIntern = document.querySelector("div.field-discount_euro_intern");

        const percent = document.querySelector("div.field-discount_percent");
        const percentIntern = document.querySelector("div.field-discount_percent_intern");

        // ❗ Initial: Alles ausblenden
        euro.style.display = "none";
        euroIntern.style.display = "none";
        percent.style.display = "none";
        percentIntern.style.display = "none";

        if (type === "euro") {
            euro.style.display = "block";
            euroIntern.style.display = "block";
        }

        if (type === "percent") {
            percent.style.display = "block";
            percentIntern.style.display = "block";
        }
    }

    document.addEventListener("DOMContentLoaded", function() {
        const select = document.getElementById("id_discount_type");
        if (select) {
            select.addEventListener("change", toggleFields);
            toggleFields(); // Initial
        }
    });
})();
