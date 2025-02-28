<template>

    <div class="container">
        <div class="row">
            <div class="col-sm-10">
                
                <h1>DangDo</h1>
                <hr><br><br>

                <button 
                    type="button" 
                    class="btn btn-success btn-sm"
                    @click="toggleAddBookModal">
                    도서 추가
                </button>
                <br><br>

                <table class="table table-hover">

                    <thead>
                        <tr>
                            <th scope="col">제목</th>
                            <th scope="col">작가</th>
                            <th scope="col">독서 여부</th>
                            <th scope="col"></th>
                        </tr>
                    </thead>

                    <tbody v-if="books.length>0">
                        <tr v-for="(book, index) in books" :key="index">
                            <td>{{ book.title }}</td>
                            <td>{{ book.author }}</td>
                            <td>
                                <span v-if="book.read">o</span>
                                <span v-else>x</span>
                            </td>
                            <td>수정|삭제|당도 올리기</td>
                        </tr>
                    </tbody>

                    <tbody v-if="books.length<1">
                        <tr>
                            <td colspan="4">도서가 없습니다. 도서를 추가해주세요!</td>
                        </tr>
                    </tbody>

                </table>

            </div>
        </div>

        <!-- Modal(add book) Start -->
        <div
            ref="addBookModal"
            class="modal fade"
            :class="{ show: activeAddBookModal, 'd-block': activeAddBookModal }"
            tabindex="-1"
            role="dialog">
            <div class="modal-dialog" role="document">
                <div class="modal-content">
                    
                    <div class="modal-header">
                        <h5 class="modal-title">도서 추가</h5>
                        <button
                            type="button"
                            class="close"
                            data-dismiss="modal"
                            aria-label="Close"
                            @click="toggleAddBookModal">
                            <span aria-hidden="true">&times;</span>
                        </button>
                    </div>

                    <div class="modal-body">
                        <form>
                            <div class="mb-3">
                                <label for="addBookTitle" class="form-label">제목 : </label>
                                <input
                                    type="text"
                                    class="form-control"
                                    id="addBookTitle"
                                    v-model="addBookForm.title"
                                    placeholder="제목">
                            </div>
                            <div class="mb-3">
                                <label for="addBookAuthor">작가 : </label>
                                <input
                                    type="text"
                                    class="form-control"
                                    id="addBookAuthor"
                                    v-model="addBookForm.author"
                                    placeholder="작가">
                            </div>
                            <div class="mb-3 form-check">
                                <input
                                    type="checkbox"
                                    class="form-check-input"
                                    id="addBookRead"
                                    v-model="addBookForm.read">
                                <label class="form-check-label" for="addBookRead">읽었어요.</label>
                            </div>
                            <div class="btn-group" role="group">
                                <button
                                    type="button"
                                    class="btn btn-primary btn-sm"
                                    @click="handleAddSubmit">
                                    등록
                                </button>
                                <button
                                    type="button"
                                    class="btn btn-danger btn-sm"
                                    @click="handleAddReset">
                                    지우기
                                </button>
                            </div>
                        </form>
                    </div>

                </div>
            </div>
        </div>
        <div v-if="activeAddBookModal" class="modal-backdrop fade show"></div>
        <!-- Modal(add book) End   -->
    </div>
    
</template>

<script>
import axios from 'axios';

export default{
    data(){
        return{
            activeAddBookModal: false,
            addBookForm: {
                title: '',
                author: '',
                read: [],
                sweet: 0,
            },
            books:[],
        };
    },
    methods:{
        addBook(payload){
            const path = 'http://localhost:5001/books';
            axios.post(path, payload)
                .then(()=>{
                    this.getBooks();
                })
                .catch((error)=>{
                    console.log(error);
                    this.getBooks();
                });
        },
        getBooks(){
            const path = 'http://localhost:5001/books';
            axios.get(path)
                .then((res)=>{
                    this.books = res.data.books;
                })
                .catch((error)=>{
                    console.error(error);
                });
        },
        initForm(){
            this.addBookForm.title = '';
            this.addBookForm.author = '';
            this.addBookForm.read = [];
        },
        handleAddReset(){
            this.initForm();
        },
        handleAddSubmit(){
            this.toggleAddBookModal();
            let read = false;
            if(this.addBookForm.read[0]){
                read = true;
            }
            const payload = {
                title: this.addBookForm.title,
                author: this.addBookForm.author,
                read,
            };
            this.addBook(payload);
            this.initForm();
        },
        toggleAddBookModal(){
            const body = document.querySelector('body');
            this.activeAddBookModal = !this.activeAddBookModal;
            if(this.activeAddBookModal){
                body.classList.add('modal-open');
            }else{
                body.classList.remove('modal-open');
            }
        },
    },
    created(){
        this.getBooks();
    },
};
</script>

<style>
    .close{
        border: none;
        background-color: white;
        margin-left: auto;
    }
</style>