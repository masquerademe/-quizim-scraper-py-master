/*
 *   Copyright (c) 2023 Jack Bennett
 *   All rights reserved.
 *
 *   Please see the LICENCE file for more information.
 */

document.addEventListener("DOMContentLoaded", () => {
    // cardset import submit event
    let importForm = document.querySelector("#setid-prompt form");

    importForm.addEventListener("submit", (e) => {
        e.preventDefault();

        let data = new FormData(importForm);

        const url = `https://quizlet.com/${data.get("setid")}/abc/`

        fetch("/flashcards", {
            method: "POST",
            body: url
        }).then((response) => {
            if (response.status == 200) {
                window.location.reload();
            }
        })
    });
});
