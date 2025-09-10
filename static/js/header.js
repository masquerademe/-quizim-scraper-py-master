/*
 *   Copyright (c) 2023 Jack Bennett
 *   All rights reserved.
 *
 *   Please see the LICENCE file for more information.
 */

const LogoSrc = "/static/img/quizim_full_col.svg";
const IconSrc = "/static/img/quizim_icon_col.svg";

export function initHeader(header) {
    let logo = header.querySelector("#header-elem-icon");
    let logoImg = logo.querySelector("img");

    let burger = header.querySelector("#header-elem-burger");
    let navbar = header.querySelector("#header-elem-navbar");

    window.addEventListener("resize", () => { updateLogoImg(logoImg) });

    // invoke logo update on page load to make sure responsive design is initialised
    updateLogoImg(logoImg);

    burger.addEventListener("click", () => {
        burger.classList.toggle("cross");
        navbar.classList.toggle("burger-expanded");
    });
}

function updateLogoImg(logoImg) {
    if (window.innerWidth < 768) {
        logoImg.src = IconSrc;
    } else {
        logoImg.src = LogoSrc;
    }

    return logoImg;
}
