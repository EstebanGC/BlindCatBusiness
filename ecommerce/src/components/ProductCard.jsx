export function ProductCard({product}) {
    return (
        <div> 
            <h1>Product: {product.productName}</h1>
            <h3>Description: {product.description}</h3>
            <h3>Price: {product.productPrice}</h3>
            <h3>Stock: {product.stock}</h3>
            <hr />
        </div>
    )
}