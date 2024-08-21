local config  = require("config")

function main(splash, args)
    splash.js_enabled=false
    splash.images_enabled = false
    assert(splash:go(args.url))
    assert(splash:wait(0.5))
    local inputuser = assert(splash:select('input[name="USER"]'))
    local inputpass = assert(splash:select('input[name="PASS"]'))
    local log       = assert(splash:select('button[type="submit"]'))

    assert(inputuser:send_text(config.USERNAME))
    assert(inputpass:send_text(config.PASSWORD))
    assert(log:send_keys('<Enter>'))
    assert(splash:wait(1))
    local home_links = assert(splash:select('ul.main-menu li a[href="/shop"]'))
    assert(home_links:mouse_click())
    assert(splash:wait(1.5))
    assert(splash:set_viewport_full())


    return{
        splash:html(),
    }

end