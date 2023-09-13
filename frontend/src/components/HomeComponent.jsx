import NavbarComponent from "./NavbarComponent";
import UploadComponent from "./UploadComponent";

function HomeComponent(){
    return(
        <div>
            <div className="">
                <div>
                    <NavbarComponent/>
                    <UploadComponent/>
                </div>
            </div>
        </div>
    )
}

export default HomeComponent;