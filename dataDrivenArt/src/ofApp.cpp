#include "ofApp.h"

//--------------------------------------------------------------
void ofApp::setup(){
	receiver.setup(PORT);

	ofDirectory dir(ofToDataPath("./images/"));

	total = dir.listDir();
	
	images.resize(total);

	for (int i = 0; i < total; i++) {
		loader.loadFromDisk(images[i], dir.getName(i));
		images[i].resize(640, 480);
	}
	cout << total << " images loaded" << endl;
}

//--------------------------------------------------------------
void ofApp::update(){
	cameraImage.load("export/export.png");
	//artImage.load("images/1.jpg");
}

//--------------------------------------------------------------
void ofApp::draw(){
	cameraImage.draw(0, ofGetHeight() / 2, ofGetWidth() / 2, ofGetHeight() / 2);
	//artImage.draw(ofGetWidth() / 2, 0, ofGetWidth(), ofGetHeight() / 2);

	while (receiver.hasWaitingMessages()) {
		ofxOscMessage m;

		receiver.getNextMessage(m);

		std::string address = m.getAddress();
		console("address") << address << " " << m.getNumArgs();

		if (m.getAddress() == "/image") {
			std::string front = "images/";
			std::string back = ".jpg";
			std::string path = front + address + back;
			console(path);
			artImage.load(path);
			artImage.draw(ofGetWidth() / 2, 0, ofGetWidth(), ofGetHeight() / 2);
		}
	}
	console.print(40, 40);
}