const express = require('express');
const multer = require('multer');
const cors = require('cors');
const path = require('path');
const fs = require('fs');

const app = express();
const port = process.env.PORT || 3000;

app.use(cors())
app.use(express.static('public'));
app.use('/uploads', express.static(path.join(__dirname,'uploads')));

const upload = multer({dest: 'uploads/'});

// upload
app.post('/upload', upload.single('file'),(req,res) =>{
	res.json({filePath: `/uploads/${req.file.filename}`})
});

// download
app.get('/download/:filename', (req,res) => {
	const file = path.join(__dirname,'uploads',req.params.filename);
	res.download(file);

});
// create uploads directory if is does not exist!
if(!fs.existsSync('uploads')){
	fs.mkdirSync('uploads')
}

app.listen(port, ()=>{
	console.log(`Server running on port ${port}`);
});
