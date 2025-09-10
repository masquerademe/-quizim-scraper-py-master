/*
 *   Copyright (c) 2023 Jack Bennett
 *   All rights reserved.
 *
 *   Please see the LICENCE file for more information.
 */

import { initHeader } from "./header.js";

document.addEventListener("DOMContentLoaded", () => {
    // initialise header events
    let header = document.querySelector("header");
    initHeader(header);
});
