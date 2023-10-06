function CompressComponent() {
    return (
        <div className="container flex flex-row justify-center place-content-center">
            <div className=" bg-red-400 block w-60 mr-20 mt-10">
                <div>
                    <button className="rounded-full bg-red-300 p-2 m-2">Upload</button>
                </div>
            </div>
            <div className="bg-blue-400 block ml-20 w-60 mt-10">
                <div>
                    <button className="rounded-full bg-blue-300 p-2 m-2">Download</button>
                </div>
            </div>
        </div>
    )
}

export default CompressComponent;