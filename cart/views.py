from django.shortcuts import render, redirect, reverse


def view_cart(request):
    """ A view that returns the cart contents page """
    return render(request, "cart.html")


def add_to_cart(request, id):
    """ Add a quantity of the specified product to the cart """
    quantity = int(request.POST.get("quantity"))
    cart = request.session.get("cart", {})
    if id in cart:
        cart[id] = int(cart[id] + quantity)
    else:
        cart[id] = cart.get(id, quantity)
    request.session["cart"] = cart
    return redirect(reverse("index"))


def adjust_cart(request, id):
    """ Adjust the quanity of a specified product by a specified amount """
    quantity = int(request.POST.get("quantity"))
    cart = request.session.get("cart", {})

    if quantity > 0:
        cart[id] = quantity
    else:
        cart.pop(id)

    request.session["cart"] = cart
    return redirect(reverse("view_cart"))
